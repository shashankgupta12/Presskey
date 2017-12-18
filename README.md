# Presskey
A keystroke dynamics based authentication system which validates users based on their typing patterns. The various modules have the following roles to play:
1. datacollect.py - Collect data from 11 users for four types of strings and store in JSON format.
2. dataprocess.py and datacleanup.py - Remove irregularities from the data since it comes from an uncontrolled source.
3. outlierdeletion.py - Remove outliers from key hold timing values.
4. calculatetimings.py - Calculate keyhold time, interkey time, and latency time from the processed data.
5. training and authentication.py - Train the model on the collected typing samples and check the accuracy of the authentication system.

All the ideas and program code used in this project are completely novel and original, and hence subject to copyright of the owner Shashank Gupta. There are 3 publications in different research journals and proceedings related to this project. Hence, copying the code, reproducing, or even borrowing ideas without notifying the author shall invite legal action.
