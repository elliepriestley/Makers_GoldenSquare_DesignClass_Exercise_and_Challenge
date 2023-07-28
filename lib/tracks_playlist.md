Single-Class Programs Design Recipe

1. Describe the Problem
Typically you will be given a short statement that does this called a user story. In industry, you may also need to ask further questions to clarify aspects of the problem.

    As a user
    So that I can keep track of my music listening
    I want to add tracks I've listened to and see a list of them.

2. Design the Class Interface
The interface of a class includes:

    The name of the class.
        TracksPlaylist()


- The design of its initializer, the parameters it takes, and their data types

        init:
            takes no parameters
            stores an empty list data type under the variable name tracks_listened_to.


- The design of any properties the user will need to read or write, and their data types
- The design of its public methods, including:
- Their names and purposes
- What parameters they take and the data types
- What they return and that data type
- Any other side effects they might have


        add_track method:
        - purpose: to store a new track in the public 'tracks_listened_to' list.
        - parameters: self, track_name. Track name is a string that represents the track to be added
        - returns: an f string telling the user that the track has been successfully added to the public tracks_listened_to list.
        - side effects: no side effects


        see_playlist method:
        - purpose: to return the public 'tracks_listened_to' list. 
        parameters: self.
        returns: the tracks_listened_to variable, which is a list data type 
        side effects: no side effects



3. Create Examples as Tests
These are examples of the class being used with different initializer arguments, method calls, and how it should behave.

For complex challenges you might want to come up with a list of examples first and then test-drive them one by one. For simpler ones you might just dive straight into writing a test for the first example you want to address.

    Test that you can successfully create an instance of the class TracksPlaylist()
    Given a new instance of the class, the user can access the tracks_listened_to variable
    user1_playlist = Task()
    user1_playlist.tracks_listened_to => []

    
    Test that the add_track method adds to the public tracks_listened_to list
    Given a track(string) #add_track adds this track to the public tracks_listened_to list
    user1_playlist = Task()
    user1_playlist.add("Cruel Summer, Taylor Swift")
    user1_playlist.tracks_listened_to => ["Cruel Summer, Taylor Swift"]

    Test that the add_method returns a string indiciating that the track has been added to the tracks_listened_to_list
    user1_playlist = Task()
    user1_playlist.add("Cruel Summer, Taylor Swift") => "The track 'Cruel Summer, Taylor Swift' has been added to your listened to playlist"

    Test that the add_method parameter track_name is a string data type, and raises an error if it is not. 
    Given the parameter 1 as the track_name:
    user1_playlist = Task()
    user1_playlist.add(1) => "track_name variable must be a string"



    Test that the see_playlist method returns the tracks_listened_to list
    Given a new instance of the class, and after adding several tracks using the #add method, #see_playlist method returns the tracks_listened_to_list as expected
        user1_playlist = Task()
        user1_playlist.add("Cruel Summer, Taylor Swift")
        user1_playlist.add("September, Earth, Wind & Fire")
        user1_playlist.see_playlist => ["Cruel Summer, Taylor Swift", "September, Earth, Wind & Fire"]

   
    

4. Implement the Behaviour
For each example you create as a test, implement the behaviour that allows the class to behave according to your example.

At this point you may wish to apply small-step test-driving to manage the complexity. This means you only write the minimum lines of the example to get the test to fail (red), then make it pass (green) and refactor, before adding another line to the test until it fails, then continue.

Then return to step 3 until you have addressed the problem you were given. You may also need to revise your design, for example if you realise you made a mistake earlier.