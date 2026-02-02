MINESWEEPER_ENV_DATA = {
    "env": "{env}",
    "agent": "You are a playing the game of Minesweeper. You will be given a two dimensional board that looks like: # # #\n# # #\n# # # , with each row of the board presented sequentially, and different rows separated by \n. The game board is represented by a grid of characters: (a) '#' indicates a hidden cell; in other words, you do not whether this cell has a mine in it or not, (b) '*' indicates a revealed empty cell, i.e., a cell marked with '*' has been revealed and it does not have any mines, and (c) digits (1 through 8) indicate the count of mines in adjacent cells (for example, if a cell has digit 3 on it, it means 3 out of 8 of its adjacent cells have mines, but it does not tell you if this particular cell has mines or not). You will be given the current board state from a user. Your task is to analyze it, apply standard Minesweeper logic, and suggest the next move(s).\n\n The rows and columns in this game use 0-based indexing, i.e., the first row is indexed by 0, the second row is indexed by 1, and so on. \n\n Provide step-by-step, short and concise reasoning for how you identify any guaranteed safe cells and guaranteed mines, then propose the final move. \n\n If multiple moves are possible, choose the most logical option. \n\n Follow these instructions carefully and maintain consistency with the rules of Minesweeper. Your goal is to reveal all the empty cells, without revealing any of the cells that has mines. You should make logical deductions to avoid cells you think can have mines, while choosing the next cell to reveal. \n\nYou should format your response as follows: <Think> Any step-by-step, short and concise thinking to strategically determine the next guess for the secret word </Think> \n<Answer> reveal row column </Answer>. Here row and col refer to the 0-index row and column that you want to reveal. \n\n The game starts now, with the following board: \n\n {agent} \n\nPlease make your first move!",
    "start_state_for_training": "You are a playing the game of Minesweeper. You will be given a two dimensional board that looks like: # # #\n# # #\n# # # , with each row of the board presented sequentially, and different rows separated by \n. The game board is represented by a grid of characters: (a) '#' indicates a hidden cell; in other words, you do not whether this cell has a mine in it or not, (b) '*' indicates a revealed empty cell, i.e., a cell marked with '*' has been revealed and it does not have any mines, and (c) digits (1 through 8) indicate the count of mines in adjacent cells (for example, if a cell has digit 3 on it, it means 3 out of 8 of its adjacent cells have mines, but it does not tell you if this particular cell has mines or not). You will be given the current board state from a user. Your task is to analyze it, apply standard Minesweeper logic, and suggest the next move(s).\n\n The rows and columns in this game use 0-based indexing, i.e., the first row is indexed by 0, the second row is indexed by 1, and so on. \n\n Provide step-by-step, short and concise reasoning for how you identify any guaranteed safe cells and guaranteed mines, then propose the final move. \n\n If multiple moves are possible, choose the most logical option. \n\n Follow these instructions carefully and maintain consistency with the rules of Minesweeper. Your goal is to reveal all the empty cells, without revealing any of the cells that has mines. You should make logical deductions to avoid cells you think can have mines, while choosing the next cell to reveal. \n\nYou should format your response as follows: <Think> Any step-by-step, short and concise thinking to strategically determine the next guess for the secret word </Think> \n<Answer> reveal row column </Answer>. Here row and col refer to the 0-index row and column that you want to reveal. \n\n The game starts now, with the following board: \n\n {initial_board_view} \n\nYour first move is predetermined (you must keep the first move same in order to proceed in the game), and it is {mandatory_first_agent_move_row} {mandatory_first_agent_move_col}. Please start playing the game!",
    "start_state_for_test": "You are a playing the game of Minesweeper. You will be given a two dimensional board that looks like: # # #\n# # #\n# # # , with each row of the board presented sequentially, and different rows separated by \n. The game board is represented by a grid of characters: (a) '#' indicates a hidden cell; in other words, you do not whether this cell has a mine in it or not, (b) '*' indicates a revealed empty cell, i.e., a cell marked with '*' has been revealed and it does not have any mines, and (c) digits (1 through 8) indicate the count of mines in adjacent cells (for example, if a cell has digit 3 on it, it means 3 out of 8 of its adjacent cells have mines, but it does not tell you if this particular cell has mines or not). You will be given the current board state from a user. Your task is to analyze it, apply standard Minesweeper logic, and suggest the next move(s).\n\n The rows and columns in this game use 0-based indexing, i.e., the first row is indexed by 0, the second row is indexed by 1, and so on. \n\n Provide step-by-step, short and concise reasoning for how you identify any guaranteed safe cells and guaranteed mines, then propose the final move. \n\n If multiple moves are possible, choose the most logical option. \n\n Follow these instructions carefully and maintain consistency with the rules of Minesweeper. Your goal is to reveal all the empty cells, without revealing any of the cells that has mines. You should make logical deductions to avoid cells you think can have mines, while choosing the next cell to reveal. \n\nYou should format your response as follows: <Think> Any step-by-step, short and concise thinking to strategically determine the next guess for the secret word </Think> \n<Answer> reveal row column </Answer>. Here row and col refer to the 0-index row and column that you want to reveal. \n\n The game starts now, with the following board: \n\n {initial_board_view} \n\nPlease make your first move!",
    "judge_prompt_agent": "{env}",
    "judge_prompt_env": None,
    "env_optional_message": "",
    "judge_prompt_suffix": "",
    "agent_optional_message": "\n\nMake your next move for this game of minesweeper. Please try to be concise. You should format your response as follows: <Think> Any step-by-step, short and concise thinking to strategically determine the next guess for the secret word </Think> \n<Answer> reveal row column </Answer>.",
    "environment_default_response": "Sorry, your response does not follow the required format of the game of Minesweeper, please try again. Please try to be concise. You should format your response as follows: <Think> Any step-by-step, short and concise thinking to strategically determine the next guess for the secret word </Think> \n<Answer> reveal row column </Answer>.",
    "max_turns": 20,
        "test": [
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 5,
                "random_mine_count": 3
            },
            "agent": {
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 7,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #\n# # # # # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 4,
                "random_mine_count": 2
            },
            "agent": {
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "rows": 7,
                "cols": 6,
                "random_mine_count": 4
            },
            "agent": {
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        }
    ],
    "train": [
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ],
                    [
                        0,
                        4
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        2
                    ],
                    [
                        4,
                        3
                    ],
                    [
                        3,
                        5
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        0,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        3
                    ],
                    [
                        3,
                        1
                    ],
                    [
                        3,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        3
                    ],
                    [
                        2,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        3
                    ],
                    [
                        1,
                        4
                    ],
                    [
                        2,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    5,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        4
                    ],
                    [
                        0,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ],
                    [
                        4,
                        4
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        1,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        2
                    ],
                    [
                        1,
                        2
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    5,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        4,
                        1
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        0
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        3
                    ],
                    [
                        4,
                        2
                    ],
                    [
                        1,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        4
                    ],
                    [
                        1,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        3
                    ],
                    [
                        4,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ],
                    [
                        5,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        0
                    ],
                    [
                        3,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        3
                    ],
                    [
                        2,
                        0
                    ],
                    [
                        0,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    5,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        2
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        3
                    ],
                    [
                        0,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        3
                    ],
                    [
                        0,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        1
                    ],
                    [
                        2,
                        2
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        3
                    ],
                    [
                        4,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        0
                    ],
                    [
                        5,
                        1
                    ],
                    [
                        2,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        3
                    ],
                    [
                        0,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        0
                    ],
                    [
                        3,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        4
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        4,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        1
                    ],
                    [
                        1,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    4,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        0,
                        3
                    ],
                    [
                        2,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        4
                    ],
                    [
                        1,
                        2
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ],
                    [
                        0,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        0
                    ],
                    [
                        1,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    4,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        0
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ],
                    [
                        0,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        4
                    ],
                    [
                        2,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        3
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ],
                    [
                        1,
                        4
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        5
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ],
                    [
                        0,
                        2
                    ],
                    [
                        4,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    5,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        1
                    ],
                    [
                        0,
                        4
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        5
                    ],
                    [
                        1,
                        5
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        4
                    ],
                    [
                        4,
                        4
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        4
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        2
                    ],
                    [
                        0,
                        0
                    ],
                    [
                        1,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    5,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        2
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ],
                    [
                        3,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ],
                    [
                        2,
                        4
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        2
                    ],
                    [
                        4,
                        2
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ],
                    [
                        1,
                        4
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        3
                    ],
                    [
                        3,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        4
                    ],
                    [
                        4,
                        4
                    ],
                    [
                        5,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        0
                    ],
                    [
                        0,
                        5
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        0
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        4
                    ],
                    [
                        1,
                        3
                    ],
                    [
                        4,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ],
                    [
                        3,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        4
                    ],
                    [
                        0,
                        2
                    ],
                    [
                        4,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ],
                    [
                        3,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        3
                    ],
                    [
                        3,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        5,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        1
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        3
                    ],
                    [
                        3,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ],
                    [
                        3,
                        3
                    ],
                    [
                        2,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        4
                    ],
                    [
                        2,
                        3
                    ],
                    [
                        4,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        5
                    ],
                    [
                        3,
                        3
                    ],
                    [
                        1,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        4
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ],
                    [
                        4,
                        4
                    ],
                    [
                        4,
                        5
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        2
                    ],
                    [
                        5,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        2
                    ],
                    [
                        0,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        5,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        0
                    ],
                    [
                        3,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        1
                    ],
                    [
                        1,
                        3
                    ],
                    [
                        4,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    5,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        1
                    ],
                    [
                        2,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        3,
                        4
                    ],
                    [
                        5,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        3
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        0
                    ],
                    [
                        2,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        5
                    ],
                    [
                        0,
                        3
                    ],
                    [
                        0,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        4,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        1
                    ],
                    [
                        3,
                        5
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ],
                    [
                        0,
                        4
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        1,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ],
                    [
                        4,
                        2
                    ],
                    [
                        4,
                        5
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        5
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        3
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        1,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        4
                    ],
                    [
                        3,
                        0
                    ],
                    [
                        0,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ],
                    [
                        4,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        0
                    ],
                    [
                        2,
                        1
                    ],
                    [
                        4,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ],
                    [
                        2,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        0
                    ],
                    [
                        4,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ],
                    [
                        0,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        3
                    ],
                    [
                        1,
                        4
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        3,
                        4
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        2
                    ],
                    [
                        3,
                        1
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        1
                    ],
                    [
                        2,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        3,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        0
                    ],
                    [
                        1,
                        1
                    ],
                    [
                        2,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        1
                    ],
                    [
                        4,
                        3
                    ],
                    [
                        4,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        4
                    ],
                    [
                        0,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        4
                    ],
                    [
                        3,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        2
                    ],
                    [
                        3,
                        5
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    5,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        4
                    ],
                    [
                        4,
                        4
                    ],
                    [
                        0,
                        5
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        0
                    ],
                    [
                        2,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ],
                    [
                        2,
                        2
                    ],
                    [
                        5,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        0
                    ],
                    [
                        5,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    5,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        3
                    ],
                    [
                        0,
                        4
                    ],
                    [
                        0,
                        5
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        4
                    ],
                    [
                        2,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        4,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ],
                    [
                        3,
                        4
                    ],
                    [
                        5,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        0
                    ],
                    [
                        2,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        2
                    ],
                    [
                        5,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    4,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        1,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        5
                    ],
                    [
                        2,
                        5
                    ],
                    [
                        5,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        1
                    ],
                    [
                        2,
                        1
                    ],
                    [
                        2,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    5,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        5
                    ],
                    [
                        1,
                        2
                    ],
                    [
                        1,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        4
                    ],
                    [
                        2,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        0
                    ],
                    [
                        4,
                        4
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    5,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ],
                    [
                        4,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        3,
                        1
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        1
                    ],
                    [
                        0,
                        3
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        3
                    ],
                    [
                        0,
                        4
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        0
                    ],
                    [
                        1,
                        1
                    ],
                    [
                        1,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        4,
                        1
                    ],
                    [
                        4,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    3
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        0
                    ],
                    [
                        4,
                        1
                    ],
                    [
                        1,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        5
                    ],
                    [
                        3,
                        5
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        2,
                        5
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        2
                    ],
                    [
                        4,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        3,
                        1
                    ],
                    [
                        0,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    5,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ],
                    [
                        1,
                        4
                    ],
                    [
                        2,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        4
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        2
                    ],
                    [
                        3,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        2
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    5,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        0,
                        4
                    ],
                    [
                        4,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        4
                    ],
                    [
                        0,
                        3
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        5
                    ],
                    [
                        1,
                        5
                    ],
                    [
                        3,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        5
                    ],
                    [
                        3,
                        1
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        2,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        1
                    ],
                    [
                        3,
                        2
                    ],
                    [
                        5,
                        5
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    4,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        0
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        4
                    ],
                    [
                        2,
                        3
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    5,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ],
                    [
                        1,
                        5
                    ],
                    [
                        3,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        2,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        5
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        4
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        4
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        0
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        3,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        3
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        4
                    ],
                    [
                        1,
                        2
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        4
                    ],
                    [
                        3,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        4
                    ],
                    [
                        4,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        1
                    ],
                    [
                        4,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ],
                    [
                        2,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        4
                    ],
                    [
                        4,
                        3
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        4
                    ],
                    [
                        3,
                        1
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ],
                    [
                        3,
                        2
                    ],
                    [
                        1,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        4
                    ],
                    [
                        5,
                        3
                    ],
                    [
                        4,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    3
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        2
                    ],
                    [
                        0,
                        5
                    ],
                    [
                        2,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        4
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        0,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ],
                    [
                        3,
                        4
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        4
                    ],
                    [
                        1,
                        1
                    ],
                    [
                        1,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    5,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        5
                    ],
                    [
                        4,
                        2
                    ],
                    [
                        5,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    5,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        4
                    ],
                    [
                        2,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        2
                    ],
                    [
                        5,
                        4
                    ],
                    [
                        1,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        0
                    ],
                    [
                        1,
                        4
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        1
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ],
                    [
                        1,
                        1
                    ],
                    [
                        3,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        5
                    ],
                    [
                        1,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        0
                    ],
                    [
                        4,
                        4
                    ],
                    [
                        3,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    5,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        3
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ],
                    [
                        2,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        4,
                        5
                    ],
                    [
                        5,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        2
                    ],
                    [
                        2,
                        0
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    5,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        3
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    4,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        3
                    ],
                    [
                        5,
                        1
                    ],
                    [
                        5,
                        5
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        0
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        4
                    ],
                    [
                        1,
                        1
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        2,
                        4
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ],
                    [
                        1,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        4
                    ],
                    [
                        3,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ],
                    [
                        3,
                        5
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        4
                    ],
                    [
                        1,
                        5
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        4,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    4,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        2,
                        4
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ],
                    [
                        0,
                        4
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ],
                    [
                        0,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    4,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ],
                    [
                        4,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        3
                    ],
                    [
                        4,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        1
                    ],
                    [
                        4,
                        5
                    ],
                    [
                        1,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        1
                    ],
                    [
                        2,
                        4
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        4,
                        1
                    ],
                    [
                        4,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        0
                    ],
                    [
                        0,
                        3
                    ],
                    [
                        5,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    4,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        1
                    ],
                    [
                        2,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        1
                    ],
                    [
                        5,
                        3
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        1
                    ],
                    [
                        3,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        1
                    ],
                    [
                        2,
                        2
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        1
                    ],
                    [
                        2,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        1
                    ],
                    [
                        2,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        3,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        1
                    ],
                    [
                        0,
                        4
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        5,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        0,
                        3
                    ],
                    [
                        4,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        4
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        2
                    ],
                    [
                        4,
                        4
                    ],
                    [
                        4,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        1
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        4
                    ],
                    [
                        2,
                        5
                    ],
                    [
                        3,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        0
                    ],
                    [
                        2,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        2
                    ],
                    [
                        2,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        4
                    ],
                    [
                        0,
                        5
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        2,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ],
                    [
                        4,
                        5
                    ],
                    [
                        3,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        0
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        2,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        4
                    ],
                    [
                        1,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        4,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        1
                    ],
                    [
                        1,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    5,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        2
                    ],
                    [
                        4,
                        4
                    ],
                    [
                        2,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        2
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        1
                    ],
                    [
                        0,
                        5
                    ],
                    [
                        5,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        0
                    ],
                    [
                        5,
                        0
                    ],
                    [
                        5,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ],
                    [
                        1,
                        0
                    ],
                    [
                        2,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ],
                    [
                        4,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        0
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ],
                    [
                        3,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        4
                    ],
                    [
                        5,
                        2
                    ],
                    [
                        3,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        0
                    ],
                    [
                        1,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        3
                    ],
                    [
                        2,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        3
                    ],
                    [
                        0,
                        1
                    ],
                    [
                        3,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        1
                    ],
                    [
                        4,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ],
                    [
                        2,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        1
                    ],
                    [
                        5,
                        1
                    ],
                    [
                        1,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        5
                    ],
                    [
                        0,
                        5
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        4
                    ],
                    [
                        1,
                        0
                    ],
                    [
                        4,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        4,
                        3
                    ],
                    [
                        2,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ],
                    [
                        0,
                        4
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        5
                    ],
                    [
                        2,
                        2
                    ],
                    [
                        2,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        0
                    ],
                    [
                        5,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    4,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ],
                    [
                        4,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        1,
                        4
                    ],
                    [
                        0,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        4
                    ],
                    [
                        4,
                        2
                    ],
                    [
                        2,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    3
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        3
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        0
                    ],
                    [
                        2,
                        3
                    ],
                    [
                        2,
                        5
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    5,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        2
                    ],
                    [
                        2,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        1
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        4
                    ],
                    [
                        4,
                        3
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        2,
                        2
                    ],
                    [
                        2,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        0
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        4
                    ],
                    [
                        1,
                        5
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        4,
                        1
                    ],
                    [
                        3,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        4
                    ],
                    [
                        3,
                        0
                    ],
                    [
                        5,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        4
                    ],
                    [
                        5,
                        1
                    ],
                    [
                        3,
                        5
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        4
                    ],
                    [
                        2,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        2
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        2
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ],
                    [
                        5,
                        4
                    ],
                    [
                        2,
                        5
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ],
                    [
                        5,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    4,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ],
                    [
                        1,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ],
                    [
                        2,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        4
                    ],
                    [
                        0,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        1
                    ],
                    [
                        4,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        0
                    ],
                    [
                        2,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ],
                    [
                        0,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        1
                    ],
                    [
                        0,
                        1
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        2
                    ],
                    [
                        2,
                        4
                    ],
                    [
                        3,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ],
                    [
                        3,
                        4
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ],
                    [
                        0,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        4
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        0
                    ],
                    [
                        1,
                        3
                    ],
                    [
                        4,
                        5
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    5,
                    3
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        0
                    ],
                    [
                        1,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        4
                    ],
                    [
                        4,
                        4
                    ],
                    [
                        1,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    5,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ],
                    [
                        3,
                        1
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    5,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        5
                    ],
                    [
                        0,
                        1
                    ],
                    [
                        1,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        3,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        1
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        3
                    ],
                    [
                        2,
                        4
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        3,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        3
                    ],
                    [
                        0,
                        3
                    ],
                    [
                        3,
                        5
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    5,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ],
                    [
                        1,
                        0
                    ],
                    [
                        4,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ],
                    [
                        2,
                        5
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    5,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        0
                    ],
                    [
                        1,
                        0
                    ],
                    [
                        3,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    5,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        0
                    ],
                    [
                        0,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    4,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        3
                    ],
                    [
                        0,
                        1
                    ],
                    [
                        5,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        4
                    ],
                    [
                        0,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        3
                    ],
                    [
                        3,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ],
                    [
                        0,
                        3
                    ],
                    [
                        4,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        2
                    ],
                    [
                        4,
                        2
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        1,
                        3
                    ],
                    [
                        4,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        4
                    ],
                    [
                        2,
                        1
                    ],
                    [
                        5,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ],
                    [
                        4,
                        2
                    ],
                    [
                        1,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        5
                    ],
                    [
                        4,
                        4
                    ],
                    [
                        4,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        5,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        2
                    ],
                    [
                        5,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    4,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        4
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        2,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ],
                    [
                        3,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ],
                    [
                        1,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        2,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        0
                    ],
                    [
                        5,
                        5
                    ],
                    [
                        2,
                        5
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    5,
                    3
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        5
                    ],
                    [
                        5,
                        2
                    ],
                    [
                        5,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        2
                    ],
                    [
                        2,
                        3
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        0
                    ],
                    [
                        4,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    4,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        0
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        4,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        1
                    ],
                    [
                        4,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    5,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ],
                    [
                        3,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ],
                    [
                        3,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ],
                    [
                        2,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        3
                    ],
                    [
                        3,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        4
                    ],
                    [
                        0,
                        4
                    ],
                    [
                        4,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ],
                    [
                        3,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        0
                    ],
                    [
                        0,
                        0
                    ],
                    [
                        2,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        5
                    ],
                    [
                        3,
                        5
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        0
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        5
                    ],
                    [
                        3,
                        4
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ],
                    [
                        1,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        2
                    ],
                    [
                        4,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    5,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        1
                    ],
                    [
                        2,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        1,
                        0
                    ],
                    [
                        0,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    5,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        0
                    ],
                    [
                        2,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        3
                    ],
                    [
                        3,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        3
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        0
                    ],
                    [
                        2,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        2
                    ],
                    [
                        3,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    4,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        1
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        1
                    ],
                    [
                        5,
                        3
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ],
                    [
                        2,
                        0
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        4
                    ],
                    [
                        4,
                        3
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        4
                    ],
                    [
                        0,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        4,
                        0
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        2
                    ],
                    [
                        4,
                        1
                    ],
                    [
                        0,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        0,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        3
                    ],
                    [
                        1,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        3,
                        3
                    ],
                    [
                        4,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    5,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        2
                    ],
                    [
                        5,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        3
                    ],
                    [
                        2,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        0,
                        0
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        4
                    ],
                    [
                        2,
                        1
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ],
                    [
                        1,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        2,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        1
                    ],
                    [
                        3,
                        0
                    ],
                    [
                        2,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ],
                    [
                        3,
                        2
                    ],
                    [
                        1,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        4
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ],
                    [
                        1,
                        0
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        4
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        2
                    ],
                    [
                        3,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        0
                    ],
                    [
                        0,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        4,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    4,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        4
                    ],
                    [
                        4,
                        2
                    ],
                    [
                        1,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ],
                    [
                        2,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        4
                    ],
                    [
                        1,
                        1
                    ],
                    [
                        0,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    5,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    4,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        0
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ],
                    [
                        2,
                        3
                    ],
                    [
                        2,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        1,
                        4
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        4
                    ],
                    [
                        2,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        4
                    ],
                    [
                        0,
                        3
                    ],
                    [
                        5,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        2
                    ],
                    [
                        1,
                        4
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        1
                    ],
                    [
                        3,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        0
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        3,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        3,
                        2
                    ],
                    [
                        3,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        5
                    ],
                    [
                        3,
                        4
                    ],
                    [
                        0,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        2,
                        1
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    5,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        2
                    ],
                    [
                        2,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        0
                    ],
                    [
                        3,
                        2
                    ],
                    [
                        4,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ],
                    [
                        5,
                        2
                    ],
                    [
                        1,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        5
                    ],
                    [
                        5,
                        0
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        5,
                        0
                    ],
                    [
                        0,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        2,
                        0
                    ],
                    [
                        4,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        0
                    ],
                    [
                        4,
                        3
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    5,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        3,
                        5
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        3,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        4
                    ],
                    [
                        4,
                        2
                    ],
                    [
                        5,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        2,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    4,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        3
                    ],
                    [
                        4,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    5,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        4
                    ],
                    [
                        4,
                        2
                    ],
                    [
                        4,
                        5
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    4,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    4,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        0
                    ],
                    [
                        5,
                        0
                    ],
                    [
                        2,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    5,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        5
                    ],
                    [
                        4,
                        1
                    ],
                    [
                        2,
                        5
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        2
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        5
                    ],
                    [
                        1,
                        4
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        0
                    ],
                    [
                        5,
                        5
                    ],
                    [
                        4,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    4,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    5,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        0
                    ],
                    [
                        2,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ],
                    [
                        3,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        3
                    ],
                    [
                        0,
                        5
                    ],
                    [
                        2,
                        5
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    5,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        1
                    ],
                    [
                        2,
                        2
                    ],
                    [
                        2,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ],
                    [
                        4,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ],
                    [
                        2,
                        0
                    ],
                    [
                        2,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    5,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        2,
                        0
                    ],
                    [
                        5,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        0,
                        2
                    ],
                    [
                        4,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        3
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ],
                    [
                        5,
                        1
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        0
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    4,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        2
                    ],
                    [
                        3,
                        4
                    ],
                    [
                        2,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        5
                    ],
                    [
                        4,
                        3
                    ],
                    [
                        2,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        0
                    ],
                    [
                        4,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        1
                    ],
                    [
                        2,
                        4
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        0
                    ],
                    [
                        2,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ],
                    [
                        2,
                        4
                    ],
                    [
                        3,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    5,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        0
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    4,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        4,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ],
                    [
                        2,
                        4
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        2,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        4
                    ],
                    [
                        5,
                        0
                    ],
                    [
                        1,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    5,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        3
                    ],
                    [
                        1,
                        2
                    ],
                    [
                        2,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ],
                    [
                        2,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        0
                    ],
                    [
                        3,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        4,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        3,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ],
                    [
                        0,
                        5
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        1
                    ],
                    [
                        4,
                        0
                    ],
                    [
                        2,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        1
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        2,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        3
                    ],
                    [
                        2,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ],
                    [
                        3,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        5
                    ],
                    [
                        1,
                        2
                    ],
                    [
                        2,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        2,
                        5
                    ],
                    [
                        2,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    5,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ],
                    [
                        1,
                        2
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        1
                    ],
                    [
                        1,
                        4
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        4
                    ],
                    [
                        4,
                        0
                    ],
                    [
                        2,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    5,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        4
                    ],
                    [
                        3,
                        0
                    ],
                    [
                        3,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ],
                    [
                        2,
                        0
                    ],
                    [
                        3,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        5
                    ],
                    [
                        1,
                        4
                    ],
                    [
                        5,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        0
                    ],
                    [
                        4,
                        1
                    ],
                    [
                        4,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        0
                    ],
                    [
                        1,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ],
                    [
                        2,
                        5
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    3
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        1
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        2
                    ],
                    [
                        5,
                        1
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        0
                    ],
                    [
                        4,
                        3
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        4
                    ],
                    [
                        2,
                        4
                    ],
                    [
                        5,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    5,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        4
                    ],
                    [
                        4,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        0
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        0
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        2,
                        4
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        1
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        4
                    ],
                    [
                        1,
                        1
                    ],
                    [
                        1,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        2
                    ],
                    [
                        2,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        4
                    ],
                    [
                        2,
                        2
                    ],
                    [
                        5,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    4,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        3,
                        3
                    ],
                    [
                        2,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ],
                    [
                        1,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        5,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        4
                    ],
                    [
                        2,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        1
                    ],
                    [
                        4,
                        4
                    ],
                    [
                        2,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        5
                    ],
                    [
                        2,
                        3
                    ],
                    [
                        5,
                        5
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        2
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        2
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        1,
                        2
                    ],
                    [
                        0,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ],
                    [
                        1,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        1
                    ],
                    [
                        4,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        1
                    ],
                    [
                        3,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        4
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        0
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        2
                    ],
                    [
                        2,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        0
                    ],
                    [
                        0,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        0
                    ],
                    [
                        5,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    4,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        0
                    ],
                    [
                        3,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ],
                    [
                        0,
                        4
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        4
                    ],
                    [
                        4,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        3
                    ],
                    [
                        2,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    4,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        0
                    ],
                    [
                        2,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ],
                    [
                        4,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        2,
                        4
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        1
                    ],
                    [
                        4,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        4
                    ],
                    [
                        1,
                        2
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        0
                    ],
                    [
                        1,
                        5
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        1,
                        4
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ],
                    [
                        4,
                        4
                    ],
                    [
                        4,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        3,
                        5
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        1,
                        0
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ],
                    [
                        2,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        1
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ],
                    [
                        1,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        5
                    ],
                    [
                        3,
                        2
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ],
                    [
                        2,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    4,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ],
                    [
                        3,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        4,
                        0
                    ],
                    [
                        1,
                        5
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        4,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ],
                    [
                        2,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        5
                    ],
                    [
                        3,
                        5
                    ],
                    [
                        1,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ],
                    [
                        3,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ],
                    [
                        1,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        1
                    ],
                    [
                        5,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        3
                    ],
                    [
                        4,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        3
                    ],
                    [
                        2,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    5,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        2,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        3
                    ],
                    [
                        3,
                        3
                    ],
                    [
                        4,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        2,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        2
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        4
                    ],
                    [
                        1,
                        5
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        0
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        4
                    ],
                    [
                        0,
                        1
                    ],
                    [
                        2,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        1
                    ],
                    [
                        1,
                        2
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        1
                    ],
                    [
                        0,
                        1
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        3
                    ],
                    [
                        5,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ],
                    [
                        3,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    5,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        0
                    ],
                    [
                        1,
                        4
                    ],
                    [
                        1,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ],
                    [
                        4,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ],
                    [
                        0,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        2,
                        0
                    ],
                    [
                        4,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ],
                    [
                        2,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        0
                    ],
                    [
                        4,
                        3
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        0
                    ],
                    [
                        3,
                        4
                    ],
                    [
                        5,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        1,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    5,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        3,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        0
                    ],
                    [
                        2,
                        2
                    ],
                    [
                        2,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        0
                    ],
                    [
                        2,
                        2
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        2,
                        4
                    ],
                    [
                        3,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        2
                    ],
                    [
                        2,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ],
                    [
                        2,
                        4
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        4
                    ],
                    [
                        5,
                        2
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        4
                    ],
                    [
                        4,
                        1
                    ],
                    [
                        1,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        4
                    ],
                    [
                        3,
                        4
                    ],
                    [
                        0,
                        5
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ],
                    [
                        3,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        4
                    ],
                    [
                        1,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        2
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        5
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        4
                    ],
                    [
                        3,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        3,
                        4
                    ],
                    [
                        5,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    5,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        5
                    ],
                    [
                        2,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        4
                    ],
                    [
                        5,
                        3
                    ],
                    [
                        3,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    5,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        2
                    ],
                    [
                        1,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        0
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ],
                    [
                        2,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        4
                    ],
                    [
                        3,
                        2
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ],
                    [
                        1,
                        5
                    ],
                    [
                        2,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ],
                    [
                        3,
                        4
                    ],
                    [
                        3,
                        5
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        4
                    ],
                    [
                        0,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        1,
                        5
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ],
                    [
                        5,
                        1
                    ],
                    [
                        2,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        1
                    ],
                    [
                        3,
                        2
                    ],
                    [
                        1,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        2,
                        4
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    4,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        0
                    ],
                    [
                        4,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ],
                    [
                        3,
                        4
                    ],
                    [
                        3,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ],
                    [
                        5,
                        2
                    ],
                    [
                        2,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        4
                    ],
                    [
                        4,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        1,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        4,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        4
                    ],
                    [
                        2,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        4
                    ],
                    [
                        2,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ],
                    [
                        4,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        1
                    ],
                    [
                        2,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        1,
                        4
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        3
                    ],
                    [
                        1,
                        1
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ],
                    [
                        2,
                        4
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        1,
                        4
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ],
                    [
                        2,
                        4
                    ],
                    [
                        4,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        2
                    ],
                    [
                        3,
                        0
                    ],
                    [
                        2,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    3
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        3
                    ],
                    [
                        1,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        3
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        1
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        2
                    ],
                    [
                        3,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        4
                    ],
                    [
                        1,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ],
                    [
                        1,
                        5
                    ],
                    [
                        4,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    5,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        1
                    ],
                    [
                        3,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        3
                    ],
                    [
                        3,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    4,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ],
                    [
                        1,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ],
                    [
                        0,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        0,
                        4
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    4,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        5
                    ],
                    [
                        2,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        3
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        0
                    ],
                    [
                        3,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        2,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ],
                    [
                        4,
                        2
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        3
                    ],
                    [
                        4,
                        1
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        2
                    ],
                    [
                        3,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        2
                    ],
                    [
                        4,
                        0
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        5
                    ],
                    [
                        0,
                        5
                    ],
                    [
                        3,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        2
                    ],
                    [
                        2,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ],
                    [
                        3,
                        2
                    ],
                    [
                        1,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        2
                    ],
                    [
                        1,
                        2
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        5,
                        4
                    ],
                    [
                        3,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        0,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ],
                    [
                        2,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ],
                    [
                        2,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        5
                    ],
                    [
                        1,
                        2
                    ],
                    [
                        2,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        3
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    5,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        1
                    ],
                    [
                        3,
                        4
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        2
                    ],
                    [
                        2,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ],
                    [
                        2,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        1,
                        2
                    ],
                    [
                        1,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        1
                    ],
                    [
                        2,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        1,
                        4
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        3,
                        0
                    ],
                    [
                        4,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    5,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        2
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    4,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        2
                    ],
                    [
                        2,
                        5
                    ],
                    [
                        5,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        4
                    ],
                    [
                        2,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        3
                    ],
                    [
                        2,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        1,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        1,
                        4
                    ],
                    [
                        4,
                        5
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        2
                    ],
                    [
                        4,
                        1
                    ],
                    [
                        4,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        2,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ],
                    [
                        1,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        5
                    ],
                    [
                        0,
                        0
                    ],
                    [
                        5,
                        5
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        4
                    ],
                    [
                        2,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ],
                    [
                        2,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        3
                    ],
                    [
                        2,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        0
                    ],
                    [
                        2,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        1
                    ],
                    [
                        4,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        5
                    ],
                    [
                        3,
                        3
                    ],
                    [
                        1,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ],
                    [
                        1,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    4,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        4
                    ],
                    [
                        4,
                        5
                    ],
                    [
                        4,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ],
                    [
                        5,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        3
                    ],
                    [
                        4,
                        0
                    ],
                    [
                        1,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        2,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        3
                    ],
                    [
                        2,
                        2
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    5,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        5
                    ],
                    [
                        4,
                        4
                    ],
                    [
                        2,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        4,
                        5
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        5,
                        1
                    ],
                    [
                        1,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        2
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        0
                    ],
                    [
                        2,
                        4
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ],
                    [
                        2,
                        5
                    ],
                    [
                        3,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        4
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        2,
                        3
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        1
                    ],
                    [
                        1,
                        4
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        1
                    ],
                    [
                        4,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        4
                    ],
                    [
                        3,
                        3
                    ],
                    [
                        0,
                        5
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        2
                    ],
                    [
                        0,
                        4
                    ],
                    [
                        1,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        3,
                        2
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        3
                    ],
                    [
                        3,
                        5
                    ],
                    [
                        1,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    5,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        0,
                        2
                    ],
                    [
                        3,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    5,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        0
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ],
                    [
                        4,
                        0
                    ],
                    [
                        3,
                        5
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        4,
                        3
                    ],
                    [
                        3,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        4
                    ],
                    [
                        4,
                        2
                    ],
                    [
                        2,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        2
                    ],
                    [
                        2,
                        0
                    ],
                    [
                        5,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ],
                    [
                        3,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        5
                    ],
                    [
                        2,
                        5
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        1,
                        2
                    ],
                    [
                        3,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        2
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ],
                    [
                        3,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        5
                    ],
                    [
                        1,
                        4
                    ],
                    [
                        1,
                        5
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    3
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ],
                    [
                        4,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    4,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        0
                    ],
                    [
                        5,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        1
                    ],
                    [
                        4,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        1
                    ],
                    [
                        4,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        2
                    ],
                    [
                        5,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        2,
                        0
                    ],
                    [
                        3,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        1,
                        4
                    ],
                    [
                        5,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        2
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ],
                    [
                        1,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        2,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ],
                    [
                        2,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        5
                    ],
                    [
                        2,
                        5
                    ],
                    [
                        3,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        0
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        5,
                        0
                    ],
                    [
                        3,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        4,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        1
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    4,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        3
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ],
                    [
                        0,
                        2
                    ],
                    [
                        4,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        0
                    ],
                    [
                        3,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        1
                    ],
                    [
                        4,
                        4
                    ],
                    [
                        3,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        0
                    ],
                    [
                        3,
                        2
                    ],
                    [
                        3,
                        5
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ],
                    [
                        4,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        5
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        0
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        0
                    ],
                    [
                        1,
                        1
                    ],
                    [
                        5,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        4
                    ],
                    [
                        2,
                        0
                    ],
                    [
                        0,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        2
                    ],
                    [
                        0,
                        2
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        1
                    ],
                    [
                        1,
                        3
                    ],
                    [
                        5,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        2
                    ],
                    [
                        2,
                        2
                    ],
                    [
                        3,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        0
                    ],
                    [
                        4,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        4
                    ],
                    [
                        1,
                        1
                    ],
                    [
                        4,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    5,
                    3
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        5
                    ],
                    [
                        0,
                        4
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    3
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        4
                    ],
                    [
                        1,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        1
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        3
                    ],
                    [
                        5,
                        4
                    ],
                    [
                        4,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        2,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        3
                    ],
                    [
                        4,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        2
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ],
                    [
                        1,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ],
                    [
                        1,
                        2
                    ],
                    [
                        4,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        3,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        5
                    ],
                    [
                        3,
                        4
                    ],
                    [
                        1,
                        5
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        4
                    ],
                    [
                        2,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ],
                    [
                        4,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        2,
                        0
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        4
                    ],
                    [
                        3,
                        4
                    ],
                    [
                        3,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ],
                    [
                        3,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        0
                    ],
                    [
                        1,
                        1
                    ],
                    [
                        0,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        0
                    ],
                    [
                        2,
                        0
                    ],
                    [
                        2,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        4
                    ],
                    [
                        2,
                        2
                    ],
                    [
                        4,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        3
                    ],
                    [
                        0,
                        0
                    ],
                    [
                        2,
                        5
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        0
                    ],
                    [
                        0,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        1
                    ],
                    [
                        1,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        1
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        2
                    ],
                    [
                        1,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ],
                    [
                        3,
                        2
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        5,
                        1
                    ],
                    [
                        1,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        2
                    ],
                    [
                        2,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        1,
                        4
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        4
                    ],
                    [
                        0,
                        5
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        0
                    ],
                    [
                        4,
                        1
                    ],
                    [
                        2,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        0
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        0
                    ],
                    [
                        4,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        4
                    ],
                    [
                        3,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        3
                    ],
                    [
                        2,
                        4
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        5,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    4,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        3,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        4
                    ],
                    [
                        4,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        2
                    ],
                    [
                        0,
                        3
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ],
                    [
                        4,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        2
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    4,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        4
                    ],
                    [
                        2,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ],
                    [
                        0,
                        1
                    ],
                    [
                        3,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ],
                    [
                        1,
                        4
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        0
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        1
                    ],
                    [
                        5,
                        3
                    ],
                    [
                        4,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    5,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    3,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    4,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        4,
                        4
                    ],
                    [
                        1,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        0
                    ],
                    [
                        0,
                        3
                    ],
                    [
                        4,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        3
                    ],
                    [
                        5,
                        2
                    ],
                    [
                        0,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        3
                    ],
                    [
                        1,
                        1
                    ],
                    [
                        5,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ],
                    [
                        3,
                        4
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ],
                    [
                        2,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    4,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        3
                    ],
                    [
                        2,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        1,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ],
                    [
                        2,
                        4
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        4
                    ],
                    [
                        4,
                        4
                    ],
                    [
                        2,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        2
                    ],
                    [
                        2,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    4,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ],
                    [
                        2,
                        4
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        0
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        2
                    ],
                    [
                        0,
                        0
                    ],
                    [
                        3,
                        5
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        3
                    ],
                    [
                        2,
                        3
                    ],
                    [
                        3,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    3
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        1
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ],
                    [
                        3,
                        3
                    ],
                    [
                        0,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        3,
                        5
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        5,
                        3
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ],
                    [
                        4,
                        4
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ],
                    [
                        0,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ],
                    [
                        4,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ],
                    [
                        5,
                        3
                    ],
                    [
                        1,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ],
                    [
                        2,
                        1
                    ],
                    [
                        2,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    1
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        0,
                        0
                    ],
                    [
                        0,
                        5
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    5,
                    3
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        4
                    ],
                    [
                        3,
                        0
                    ],
                    [
                        5,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        1
                    ],
                    [
                        0,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        0,
                        4
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        4
                    ],
                    [
                        1,
                        4
                    ],
                    [
                        1,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    5,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        4
                    ],
                    [
                        0,
                        1
                    ],
                    [
                        3,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        0
                    ],
                    [
                        4,
                        3
                    ],
                    [
                        5,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ],
                    [
                        2,
                        0
                    ],
                    [
                        1,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ],
                    [
                        4,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        2
                    ],
                    [
                        3,
                        4
                    ],
                    [
                        3,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        5
                    ],
                    [
                        2,
                        4
                    ],
                    [
                        5,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        4,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ],
                    [
                        3,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        3
                    ],
                    [
                        2,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ],
                    [
                        3,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        4
                    ],
                    [
                        2,
                        5
                    ],
                    [
                        2,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ],
                    [
                        4,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    5,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ],
                    [
                        0,
                        2
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        0,
                        2
                    ],
                    [
                        5,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    4,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ],
                    [
                        4,
                        1
                    ],
                    [
                        5,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        2,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        2
                    ],
                    [
                        1,
                        4
                    ],
                    [
                        0,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    5,
                    4
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        5,
                        1
                    ],
                    [
                        0,
                        4
                    ],
                    [
                        3,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        1,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        1,
                        1
                    ],
                    [
                        0,
                        5
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    3
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        4
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        1
                    ],
                    [
                        3,
                        4
                    ],
                    [
                        2,
                        5
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        2
                    ],
                    [
                        1,
                        3
                    ],
                    [
                        2,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    5,
                    0
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        5
                    ],
                    [
                        3,
                        5
                    ],
                    [
                        4,
                        1
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    1,
                    3
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        3
                    ],
                    [
                        4,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    5,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ],
                    [
                        4,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        0
                    ],
                    [
                        5,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    5,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        0
                    ],
                    [
                        0,
                        2
                    ],
                    [
                        4,
                        2
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        1
                    ],
                    [
                        4,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ],
                    [
                        1,
                        5
                    ],
                    [
                        3,
                        5
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    5
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        0
                    ],
                    [
                        0,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        1
                    ],
                    [
                        1,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        2
                    ],
                    [
                        2,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        1
                    ],
                    [
                        2,
                        2
                    ],
                    [
                        5,
                        4
                    ]
                ],
                "rows": 6,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    0,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        3
                    ],
                    [
                        3,
                        1
                    ],
                    [
                        1,
                        5
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    4,
                    4
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        0
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ],
                    [
                        3,
                        3
                    ]
                ],
                "rows": 4,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    2,
                    2
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        0,
                        2
                    ],
                    [
                        4,
                        3
                    ],
                    [
                        2,
                        1
                    ]
                ],
                "rows": 5,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    0,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        0,
                        4
                    ]
                ],
                "rows": 5,
                "cols": 5
            },
            "agent": {
                "first_agent_move": [
                    1,
                    1
                ],
                "initial_board_view": "# # # # #\n# # # # #\n# # # # #\n# # # # #\n# # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ],
                    [
                        3,
                        4
                    ]
                ],
                "rows": 4,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    2,
                    3
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ],
                    [
                        1,
                        2
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        2
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    0,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        3,
                        1
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    0
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ],
                    [
                        0,
                        3
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    3
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        4
                    ],
                    [
                        2,
                        2
                    ],
                    [
                        0,
                        5
                    ]
                ],
                "rows": 6,
                "cols": 6
            },
            "agent": {
                "first_agent_move": [
                    5,
                    0
                ],
                "initial_board_view": "# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #\n# # # # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        3
                    ],
                    [
                        1,
                        3
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        4,
                        2
                    ],
                    [
                        5,
                        0
                    ]
                ],
                "rows": 6,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    1,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        2,
                        0
                    ],
                    [
                        1,
                        0
                    ]
                ],
                "rows": 5,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    2,
                    1
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #\n# # # #"
            }
        },
        {
            "env": {
                "mine_positions": [
                    [
                        1,
                        1
                    ]
                ],
                "rows": 4,
                "cols": 4
            },
            "agent": {
                "first_agent_move": [
                    3,
                    2
                ],
                "initial_board_view": "# # # #\n# # # #\n# # # #\n# # # #"
            }
        }
    ]
}