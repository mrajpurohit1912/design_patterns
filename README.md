#This Repository is a for practice of basic implementation of design patterns in python

What is design pattern?
-> Software design pattern is a general,reusable solution to a commanly occuring problems while developting a software


1. Creational Patterns
These patterns focus on object creation mechanisms, ensuring objects are created in a controlled and efficient way.

Purpose: To abstract the instantiation process and make a system independent of how its objects are created.
Examples:

Singleton: Ensures only one instance of a class exists.
Factory Method: Defines an interface for creating an object but lets subclasses alter the type of objects created.
Abstract Factory: Provides an interface for creating families of related or dependent objects.
Builder: Separates the construction of a complex object from its representation.
Prototype: Creates a new object by copying an existing object.



2. Structural Patterns
These patterns deal with the composition of classes and objects to form larger structures while keeping the system flexible and efficient.

Purpose: To simplify the relationships between entities in a system.
Examples:

Adapter: Allows incompatible interfaces to work together.
Bridge: Separates an object’s abstraction from its implementation so that they can vary independently.
Composite: Composes objects into tree structures to represent part-whole hierarchies.
Decorator: Dynamically adds responsibilities to an object without modifying its structure.
Facade: Provides a unified interface to a set of interfaces in a subsystem.
Flyweight: Reduces the cost of creating and managing a large number of similar objects.
Proxy: Provides a surrogate or placeholder for another object.



3. Behavioral Patterns
These patterns focus on the interaction and responsibility among objects.

Purpose: To simplify communication between objects and control the flow of a program.
Examples:

Observer: Defines a one-to-many dependency so that when one object changes state, all its dependents are notified.
Strategy: Defines a family of algorithms, encapsulates them, and makes them interchangeable.
Command: Encapsulates a request as an object, allowing parameterization of clients with queues, requests, and operations.
Chain of Responsibility: Passes requests along a chain of handlers.
State: Allows an object to alter its behavior when its internal state changes.
Template Method: Defines the skeleton of an algorithm in a method but lets subclasses override specific steps.
Mediator: Reduces coupling between classes by introducing a mediator that handles communication.
Iterator: Provides a way to access elements of a collection sequentially without exposing the underlying structure.