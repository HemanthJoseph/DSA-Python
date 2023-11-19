#include<iostream>

/**
* @brief A class to create a new Node
*/
class Node{
    public:
        int data;
        Node* next;

        // Class constructor with default values
        Node(int data=0, Node* next=nullptr) : data(data), next(next) {}
};

/**
* @brief A class for creating a Linked List
*/
class LinkedList{
    private:
        Node* head;
    
    public:


        /*
        Class constructors and desctructors
        */

        // Class Constructor for LinkedList
        LinkedList() : head(nullptr){}

        // Class Destructor for LinkedList
        ~LinkedList(){
            while (head != nullptr){
                Node* temp = head;
                head = head->next;
                delete temp;
            }
        }



        /*
        Class methods
        */
        // Method to print the LinkedList
        void printList(){
            Node* current = head;
            while (current != nullptr){
                std::cout << current->data << "->";
                current = current->next;
            }
            std::cout << std::endl;
        }

        // Method to get length of a class
        int getLength(){
            int length = 0;
            Node* current = head;

            while (current != nullptr){
                length++;
                current = current->next;
            }
            return length;
        }

        // Method to insert at the beginning
        void insertAtBeginning(int newData){
            Node* newNode = new Node(newData, head);
            head = newNode;
        }

        // Method to insert at the end
        void insertAtEnd(int newData){
            Node* newNode = new Node(newData);
            if (head == nullptr){
                head = newNode;
                return;
            }

            Node* current = head;
            while (current->next != nullptr){
                current = current->next;
            }
            current->next = newNode;
        }

        // Method to insert at a particular index
        void insertAtIndex(int index, int newData){
            if (index < 0 || index > getLength()){
                std::cerr << "Index is out of bounds\n";
                return;
            }
            if (index == 0){
                insertAtBeginning(newData);
                return;
            }
            Node* newNode = new Node(newData);
            Node* current = head;

            for(int i = 0; i < index-1; ++i){
                current = current->next;
            }

            newNode->next = current->next;
            current->next = newNode;
        }

        // Method to delete at a particular index
        void deleteAtIndex(int index){
            if (index < 0 || index >= getLength() || head == nullptr){
                std::cerr << "Index is out of bounds\n";
                return;
            }
            Node* temp;
            if (index ==0){
                temp = head;
                head = head->next;
            } else {
                Node* current = head;
                for(int i = 0; i<index-1; ++i){
                    current = current->next;
                }
                temp = current->next;
                current->next = temp->next;
            }
            delete temp;
        }
};


int main(){

    std::cout << "Beginning Implementing Linked List\n";

    LinkedList my_linked_list;

    my_linked_list.insertAtEnd(10);
    my_linked_list.insertAtEnd(20);
    my_linked_list.insertAtEnd(55);

    std::cout << "Original Linked List: ";
    my_linked_list.printList();

    my_linked_list.insertAtBeginning(5);
    std::cout << "Linked List after inserting value at the beginning: ";
    my_linked_list.printList();

    my_linked_list.insertAtIndex(3, 98);
    std::cout << "Linked List after inserting value at index 3: ";
    my_linked_list.printList();

    my_linked_list.deleteAtIndex(2);
    std::cout << "Linked List after deleting value at index 2: ";
    my_linked_list.printList();

    return 0;
}