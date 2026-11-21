# Iterated Prisoner's Dilemma
 
A simple Python simulation of the iterated prisoner's dilemma.
Two strategies play a number of rounds against each other, and the total score of each player is returned.
 
## Files
 
- `payoffTable.py`: the payoff table (`pointsTable`) and `playRound`, which returns the points of both players for one pair of moves.
- `strategyFunctions.py`: the strategies: `alwaysCooperate`, `alwaysDefect`, `alwaysRandom` and `titForTat`. Each strategy gets the game history and its player index (1 or 2), and returns `"Cooperate"` or `"Defect"`.
- `playGame.py`: `playGame(strategy1, strategy2, rounds, game)`, which plays the rounds and returns the total score of each player.
- `runGames.py`: runs three example games and records the results in comments.
- `tests.py`: tests written with `assert`.

## Strategies

- 'alwaysCooperate': always cooperates, no matter what the opponent did. The most trusting strategy, and easy to exploit.
- 'alwaysDefect': always defects, no matter what the opponent did. The most selfish strategy.
- 'alwaysRandom': chooses “Cooperate” or “Defect” at random each round (reproducible thanks to 'random.seed(42)' in runGames.py).
- 'titForTat': cooperates on the first round, then copies the opponent’s last move. It rewards cooperation and punishes defection right away.

## How to run
 
Run all commands from the project folder:
 
```
python3 runGames.py
python3 tests.py
```
 
`runGames.py` prints the results of three games.
`tests.py` prints nothing if all tests pass. If a test fails, an `AssertionError` is shown.
 
## Example results
 
| Game | Rounds | Result (player 1, player 2) |
|---|---|---|
| alwaysCooperate vs alwaysDefect | 3 | (0, 15) |
| titForTat vs alwaysDefect | 5 | (4, 9) |
| alwaysRandom vs titForTat | 7 | (20, 20) |
 
## Reproducibility
 
`alwaysRandom` makes random choices, so `runGames.py` calls `random.seed(42)` before the games. A fixed seed produces the same sequence of "random" numbers on every run, so anyone who clones the repository gets the same results.
 
---
 
# דילמת האסיר החוזרת
 
סימולציה פשוטה בפייתון של דילמת האסיר החוזרת. שתי אסטרטגיות משחקות זו מול זו מספר סיבובים, והתוכנית מחזירה את הניקוד הכולל של כל שחקן.
 
## קבצים
 
- `payoffTable.py`: טבלת הניקוד (`pointsTable`) והפונקציה `playRound`, שמחזירה את הניקוד של שני השחקנים עבור זוג מהלכים אחד.
- `strategyFunctions.py`: האסטרטגיות: `alwaysCooperate`, `alwaysDefect`, `alwaysRandom` ו-`titForTat`. כל אסטרטגיה מקבלת את היסטוריית המשחק ואת מספר השחקן (1 או 2), ומחזירה `"Cooperate"` או `"Defect"`.
- `playGame.py`: הפונקציה `playGame(strategy1, strategy2, rounds, game)`, שמריצה את הסיבובים ומחזירה את הניקוד הכולל של כל שחקן.
- `runGames.py`: מריץ שלושה משחקים לדוגמה, והתוצאות רשומות בהערות.
- `tests.py`: בדיקות שנכתבו עם `assert`.

## אסטרטגיות

- 'alwaysCooperate': תמיד משתפת פעולה, בלי קשר למה שהיריב עשה. האסטרטגיה הכי סומכת על אחרים, וקל לנצל אותה.
- 'alwaysDefect': תמיד בוגדת, בלי קשר למה שהיריב עשה. האסטרטגיה הכי אנוכית.
- 'alwaysRandom': בוחרת בכל סיבוב באקראי בין “Cooperate” ל-“Defect” (התוצאות ניתנות לשחזור בזכות 'random.seed(42) ב-runGames.py)'.
- 'titForTat': משתפת פעולה בסיבוב הראשון, ואחר כך מעתיקה את המהלך האחרון של היריב. היא מתגמלת שיתוף פעולה ומענישה בגידה מיד.

## איך מריצים
 
מריצים מתוך תיקיית הפרויקט:
 
```
python3 runGames.py
python3 tests.py
```
 
`runGames.py` מדפיס את התוצאות של שלושה משחקים. `tests.py` לא מדפיס כלום אם כל הבדיקות עברו. אם בדיקה נכשלת, מוצגת שגיאת `AssertionError`.
 
## שחזור תוצאות
 
`alwaysRandom` מקבלת החלטות אקראיות, ולכן `runGames.py` קורא ל-`random.seed(42)` לפני המשחקים. seed קבוע מייצר את אותה סדרה של מספרים "אקראיים" בכל הרצה, ולכן כל מי שמוריד את הריפו מקבל את אותן תוצאות.
 