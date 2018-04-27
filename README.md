# stack-queue-war-game
This is a final project for a class in Data Structures and Algorithms using Python and C++ |  (CSC 236) #ExtraCredit 

THE NOTION BEHIND THE GAME: HOW IT IS PLAYED

A deck of cards has 10 cards - 0 1 2 3 4 5 6 7 8 9
The game uses 2 sets of this deck, so 20 cards

Each player will have their own playing pile of cards and their own storage pile of cards
There is a single common loot pile in the center of the table
There is also a dealing pile

The "dealer" starts by picking 2 new decks of cards and then shuffles them
After shuffling the cards, the dealer will add them one by one to the top of the dealing pile
20 cards will be dealt one by one from the top of the dealing pile to the top of each playing pile alternating between playing piles

After the cards are dealt, there will be 10 cards in each playing pile
These cards are kept face-down in the respective playing piles
The storage piles for both players will be empty

In each round of play, both players will remove a card from the top of their playing piles
They then display them face-up on the table where they can be seen by both players

Whenever a player's playing pile becomes empty, her or she will immediately try to refill her playing pile by completely emptying his or her storage pile
The newly refilled playing pile should have the cards in the same order as the existing storage pile
But, the cards must be moved one by one

[EACH ROUND OF PLAY]
In each round of play:

If one player displays a higher ranking card, he or she will collect both of the displayed cards, and will add them one at a time to the top of his or her storage pile
If both players display cards of the same value (eg. each player displays a 9 card), this will start a "War" in this round of play

When "War" breaks out, the following happens:

The single loot pile located in the middle of the table will be used, and the two cards of the same value will be added to the top of the loot pile
Both players will then remove an additional card from the top of their playing pile and add them to the top of the loot pile without looking at them
Then each player will remove one additional card from his or her playing pile, and will display it face-up on the table

These two newly displayed cards will determine what happens next:

If these newly displayed cards differ, the player who displayed the higher ranking card will win all six cards
If these two newly displayed cards are two more identically numbered cards, the state of "War" will continue
The loot pile will continue to grow until there is a winner who will take the two displayed cards as well as the entire loot pile
Thus, removing all of the cards from the loot pile one by one and adding all of these cards to his or her storage pile until the loot pile is empty

If a player's playing pile and storage pile both become empty at the same time, he or she had run out of cards and immediately loses the game
In other words, rounds of play continues until one player has all 20 of the original cards
