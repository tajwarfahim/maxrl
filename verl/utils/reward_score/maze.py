import numpy as np
from typing import List, Tuple, Optional, Dict, Any

class MazeEnv:
    """
    Maze environment for simulating action execution and checking success.
    
    Implementation:
    - Maintains grid, start position, goal position, and current position
    - step() executes a single action
    - check_success() simulates a sequence of actions
    """
    
    # Action mapping: action name -> (row_delta, col_delta)
    ACTION_MAP = {
        "UP": (-1, 0),
        "DOWN": (1, 0),
        "LEFT": (0, -1),
        "RIGHT": (0, 1),
    }
    
    def __init__(
        self,
        grid: np.ndarray,
        start: Tuple[int, int],
        goal: Tuple[int, int],
    ):
        """
        Args:
            grid: Maze grid, 1 = wall, 0 = path
            start: Start position (row, col)
            goal: Goal position (row, col)
        """
        self.grid = grid
        self.size = grid.shape[0]
        self.start = start
        self.goal = goal
        self.current_pos = start
    
    def reset(self) -> Tuple[int, int]:
        """
        Reset environment to initial state.
        
        Returns:
            Start position
        """
        self.current_pos = self.start
        return self.current_pos
    
    def step(self, action: str) -> Tuple[Tuple[int, int], bool, bool]:
        """
        Execute a single action.
        
        Args:
            action: Action name (UP/DOWN/LEFT/RIGHT)
        
        Returns:
            (new_pos, done, success)
            - new_pos: New position
            - done: Whether episode ended (reached goal or hit wall)
            - success: Whether successfully reached goal
        """
        if action not in self.ACTION_MAP:
            # Invalid action, stay in place
            return self.current_pos, True, False
        
        dr, dc = self.ACTION_MAP[action]
        new_row = self.current_pos[0] + dr
        new_col = self.current_pos[1] + dc
        
        # Check boundary
        if not (0 <= new_row < self.size and 0 <= new_col < self.size):
            # Out of bounds, fail
            return self.current_pos, True, False
        
        # Check wall collision
        if self.grid[new_row, new_col] == 1:
            # Hit wall, fail
            return self.current_pos, True, False
        
        # Move to new position
        self.current_pos = (new_row, new_col)
        
        # Check if reached goal
        if self.current_pos == self.goal:
            return self.current_pos, True, True
        
        return self.current_pos, False, False
    
    def check_success(self, actions: List[str]) -> bool:
        """
        Simulate a sequence of actions and check if goal is reached.
        
        Args:
            actions: List of actions
        
        Returns:
            Whether successfully reached goal
        """
        self.reset()
        
        for action in actions:
            _, done, success = self.step(action)
            if done:
                return success
        
        # Check if at goal position after all actions
        return self.current_pos == self.goal
    
    @classmethod
    def from_sequence(cls, sequence: str) -> Optional["MazeEnv"]:
        """
        Parse and create MazeEnv from training data sequence.
        
        Implementation:
        1. Parse grid tokens between GRID_START and GRID_END
        2. Reconstruct grid from WALL/PATH/START/GOAL/NEWLINE tokens
        
        Args:
            sequence: Training data sequence string
        
        Returns:
            MazeEnv instance, or None if parsing fails
        """
        tokens = sequence.split()
        
        # Find GRID_START and GRID_END positions
        try:
            grid_start_idx = tokens.index("GRID_START")
            grid_end_idx = tokens.index("GRID_END")
        except ValueError:
            return None
        
        # Extract grid tokens
        grid_tokens = tokens[grid_start_idx + 1:grid_end_idx]
        
        # Parse grid
        rows = []
        current_row = []
        start = None
        goal = None
        
        for i, token in enumerate(grid_tokens):
            if token == "NEWLINE":
                if current_row:
                    rows.append(current_row)
                    current_row = []
            elif token in ("WALL", "PATH", "START", "GOAL"):
                row_idx = len(rows)
                col_idx = len(current_row)
                
                if token == "WALL":
                    current_row.append(1)
                else:
                    current_row.append(0)
                    if token == "START":
                        start = (row_idx, col_idx)
                    elif token == "GOAL":
                        goal = (row_idx, col_idx)
        
        # Add last row (if not ended with NEWLINE)
        if current_row:
            rows.append(current_row)
        
        if not rows or start is None or goal is None:
            return None
        
        # Convert to numpy array
        grid = np.array(rows, dtype=int)
        
        return cls(grid=grid, start=start, goal=goal)
    
    @classmethod
    def from_token_ids(
        cls,
        token_ids: List[int],
        vocab: Dict[str, int],
    ) -> Optional["MazeEnv"]:
        """
        Parse and create MazeEnv from token id sequence.
        
        Args:
            token_ids: Token id sequence
            vocab: Vocabulary dictionary
        
        Returns:
            MazeEnv instance, or None if parsing fails
        """
        # Reverse vocab dictionary
        id_to_token = {v: k for k, v in vocab.items()}
        
        # Convert to token strings
        tokens = [id_to_token.get(tid, "<unk>") for tid in token_ids]
        sequence = " ".join(tokens)
        
        return cls.from_sequence(sequence)
    
    def render_ascii(self) -> str:
        """
        Render maze as ASCII string.
        """
        chars = {1: '#', 0: ' '}
        lines = []
        lines.append("-" * (self.size + 2))
        
        for r in range(self.size):
            row_chars = []
            for c in range(self.size):
                if (r, c) == self.current_pos:
                    row_chars.append('A')  # Agent
                elif (r, c) == self.start:
                    row_chars.append('S')
                elif (r, c) == self.goal:
                    row_chars.append('G')
                else:
                    row_chars.append(chars[self.grid[r, c]])
            lines.append("|" + "".join(row_chars) + "|")
        
        lines.append("-" * (self.size + 2))
        return "\n".join(lines)


def judge_maze(solution_str: str, ground_truth: str) -> float:
    """
    Compute reward for model-generated trajectory.
    
    Args:
        solution_str: Model-generated trajectory. Format: actions + DONE + (anything after)
                      e.g., "DOWN DOWN RIGHT RIGHT DONE" or "DOWN DOWN RIGHT RIGHT DONE <eos>"
                      Actions must be UP/DOWN/LEFT/RIGHT only.
        ground_truth: Complete maze sequence, e.g., "<bos> GRID_START WALL ... GRID_END PATH_START ... DONE <eos>"
    
    Returns:
        reward: 1.0 if successfully reached goal, 0.0 if format error or failed
    """
    valid_actions = {"UP", "DOWN", "LEFT", "RIGHT"}
    
    # 1. Parse action sequence: find DONE and extract actions before it
    tokens = solution_str.strip().split()
    
    # Find DONE position
    try:
        done_idx = tokens.index("DONE")
    except ValueError:
        # No DONE found, format error
        return 0.0
    
    # Extract actions before DONE
    actions = tokens[:done_idx]
    
    # Check if all actions are valid
    for action in actions:
        if action not in valid_actions:
            # Invalid token in action sequence, format error
            return 0.0
    
    # 2. Create environment from maze string
    env = MazeEnv.from_sequence(ground_truth)
    if env is None:
        return 0.0  # Parsing failed
    
    # 3. Check success
    success = env.check_success(actions)
    
    return 1.0 if success else 0.0
