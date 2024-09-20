## How to: Make your own bot
In Bottled AI, a bot Strategy is a collection of configurations that make up its behavior. Some configurations are straightforward, like "what character do we play?" or "what cards do we pick up?".
Others are a little more complicated, like "how do we weigh damaging opponents vs powering ourselves up?".

Changing a Strategy's configurations lets you customize your own bot.

### Create a new bot Strategy
1) Go to `\rs\ai`
2) Copy the entire `_example` folder
3) Rename example.py and EXAMPLE_STRATEGY to match your new Strategy's name
4) Search for `_example` imports and rename them
5) (Change the Strategy that is run in `main.py`)

### Basics
- Come up with an idea of how you want the bot to behave
- Adjust the lists in your Strategy's `config.py` file and your strategy's handlers.

### State of Bottled AI
Important! For the current state of Bottled AI's capabilities, see [capabilities.py](capabilities.py).


## Advanced
### Handlers
Handlers contain sets of behavior to be applied when their `can_handle` conditions are applied.
There are a set of Common handler shared between Strategies, but you can create new handlers on a Strategy level.
Remember to adjust which handlers are used in your `[your_strategy's_name.py]`.

### Battle
Battles are the most complicated part of the bot. In battle, the bot will simulate/calculate the outcome from playing all of its cards in all possible configurations. We call this part the 'calculator'. Secondly, the bot will then play cards based on which plays led to the most desirable outcome.

There are therefore 2 ways to adjust in-battle behavior:
1) **Extending the simulation**: i.e. teaching the bot what happens when a card is played / relic triggered / etc. Place to start: `\rs\calculator\battle_state`.
2) **Changing the desirability of outcomes** to impact its decision-making. Place to start: `\rs\common\comparators\common_general_comparator.py`

### Other
- If you're making deeper behavior adjustments, we recommend adding some tests covering your new functionality See `/tests`
- TODO probably more