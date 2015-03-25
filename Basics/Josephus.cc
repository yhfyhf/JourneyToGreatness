int jos1( int people, int passes )
{
    list<int> theList;
    list<int>::iterator itr;
    list<int>::iterator next;
    int i;

      // Construct the list.
    for( i = 1; i <= people; i++ )
        theList.push_back( i );

      // Play the game.
    for( itr = theList.begin( ); people-- != 1; itr = next )
    {
        for( i = 0; i < passes; i++ )
        {
            ++itr;                       // Advance
            if( itr == theList.end( ) )  // If past last player
                itr = theList.begin( );  // then go to first
        }

        next = itr;       // Maintain next node, for
        ++next;           // player who is after removed player 

        theList.erase( itr );            // Remove player

        if( next == theList.end( ) )     // Set next
            next = theList.begin( );
    }

    return *itr;     // Return player's number
}
