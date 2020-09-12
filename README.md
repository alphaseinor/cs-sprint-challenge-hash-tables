# Sprint Challenge: Hash Tables

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This challenge allows you to practice the concepts and techniques learned over the past sprint and apply them in a concrete project. This sprint explored hash tables. During this sprint, you studied hash functions, collision resolution, complexity analysis of hash tables, load factor, resizing, and various use cases for hash tables. In your challenge this week, you will demonstrate mastery of these skills by solving five problems related to hash tables.

The sprint challenge is an individual assessment. All work must be your own. Your challenge score is a measure of your ability to work independently using the material covered through this sprint. You need to demonstrate proficiency in the concepts and objectives introduced and practiced in preceding days.

You are not allowed to collaborate during the sprint challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your TL if you need direction.

_You have **three hours** to complete this challenge. Plan your time accordingly._

## Introduction

This challenge requires you to solve algorithm problems that are amenable to being solved efficiently with a hash table.

### Commits

Commit your code regularly and meaningfully. This practice helps both you (in case you ever need to return to old code for any number of reasons) and your Team Lead as they evaluate your solution.

## Interview Questions

Be prepared to demonstrate your understanding of this week's concepts by answering questions on the following topics. You might prepare by writing down your answers beforehand.

Hashing functions

A hash is just encoded data of a fixed size from data that has a variable size. A hash function generates this encoded data. 
This encoded data must be predictable. 
If an identical input is entered, output from the first encoded data must match the second, or subsequent data
Typically this is stored in a table that can be accessed directly as an O(n + a), which is as close to constant time as you can get. 

Collision resolution

A collision happens when two or more items have hashed to the same value, and then tried to be stored in the same location, If you have a collision, you can store this information in a list, or a linked list, there’s also other options of direct access (but has o(n log n) as a linked list in the end).  
Different ways of hashing can reduce collision resolution assuming 
the encoding is reversible
the encoding is unique, or almost unique
SHA based encryption typically will not have collisions with most strings, which is why encoding using a SHA based algorithm is popular with applications like github. 

Load factor

Load factor is just the number of buckets and the depth of the buckets, typically the ratio should be between .7 and .25 as per our instruction. 

Performance of basic hash table operations

The reason why I added the load factor previous to this section (unlike what’s in the sprint)
resize is O(n) because it has to be rehashed
put, delete is O(1), except where put needs to resize.


Automatic resizing
sometimes called dynamic resizing, as the load factor increases, the number of collisions will increase. once you have a collision, it will decrease the performance of the table. typically this is done by iterating over the old hash table and add each entry into a new table


Various use cases for hash tables
My favorite implementation of a hash table so far is git, however it’s also used in crypto. I would imagine databases use hashing as well for faster queries. 


We expect you to be able to answer questions in these areas. Your responses contribute to your Sprint Challenge grade.

## Instructions

### Task 1: Project Set-Up

- [ ] Create a forked copy of this project
- [ ] Add your team lead as a collaborator on Github
- [ ] Clone your OWN version of the repository (Not Lambda's by mistake!)
- [ ] Create a new branch: git checkout -b `<firstName-lastName>`.
- [ ] Implement the project on your newly created `<firstName-lastName>` branch, committing changes regularly
- [ ] Push commits: git push origin `<firstName-lastName>`

### Task 2: Project Requirements

Your finished project must include all of the following requirements:

- [ ] Solve any three of the five problems

For each problem that you choose to solve, complete the following:

- [ ] Navigate into each exercise's directory
- [ ] Read the instructions for the exercise in the README
- [ ] Implement your solution in the `.py` skeleton file
- [ ] Make sure your code passes the tests running the test script with make tests

*Note: For these exercises, we expect you to use Python's built-in `dict` as a hashtable. That said, if you wish, you can attempt to solve using your own hashtable implementation, as well. All solutions should utilize a `dict` or hashtable. You should not use Sets. (Though you can make a `dict` behave like a set if you wish.)*

### Task 3: Stretch Goals

After finishing your required elements, you can push your work further. These goals may or may not be things you have learned in this module, but they build on the material you just studied. Time allowing, stretch your limits, and see if you can deliver on the following optional goals:

- [ ] Solve any four of the five problems
- [ ] Solve all five problems

## Submission format

Follow these steps to complete your project.

- [ ] Submit a Pull-Request to merge <firstName-lastName> Branch into master (student's  Repo). **Please don't merge your own pull request**
- [ ] Add your team lead as a reviewer on the pull-request
- [ ] Your team lead will count the project as complete after receiving your pull-request
