#include<iostream>
#include<string>
using namespace std;

struct Node
{
    int PRN;
    string name;
    Node *next;
};

Node *createnode()
{
    Node *ntemp=new Node;
    cout<<"Enter PRN :- ";
    cin>>ntemp->PRN;
    cout<<"Enter Name :- ";
    cin>>ntemp->name;
    ntemp->next=NULL;
    return ntemp;
}

class sll
{
    public:
        Node *start;
        sll()
        {
            start=NULL;
        }
        void create();
        void display();
        void insertatbeginning();
        void insertatend();
        void insertafter();
        void deleteatstart();
        void deleteatend();
        void deletemember();
        void printtotal();
        void concat(sll l);
};


void sll::create()
{

    int n;
    if(start==NULL){
        cout<<"Enter the no. of Members :- ";
        cin>>n;
        for(int i=0;i<n;i++){
            if(i==0)    cout<<"\nEnter the details of President "<<endl;
            else if(i==n-1) cout<<"\nEnter the details of Secretary "<<endl;
            else if(i==1)   cout<<"\nEnter the details of other members"<<endl;
            Node *ntemp=createnode();
            if(start==NULL)
            {
                start=ntemp;
            }
            else{
                Node *trav=start;
                while(trav->next!=NULL)
                    trav=trav->next;
                trav->next=ntemp;
            }
        }
        cout<<"\nlist Created :- "<<endl;
    }
    else
        cout<<"list already created try adding members "<<endl;
}

void sll::display()
{
    Node *trav=start;
    cout<<"PRN \t\t Name"<<endl;
    while(trav!=NULL)
    {
        cout<<" "<<trav->PRN<<"   \t"<<trav->name<<endl;
        trav=trav->next;
    }
}

void sll::insertatbeginning()
{
    cout<<"Enter the details of President "<<endl;
    Node *ntemp=createnode();
    ntemp->next=start;
    start=ntemp;
    
}

void sll::insertatend()
{
    cout<<"\nEnter the details of secretary "<<endl;
    Node *ntemp=createnode();
    Node *trav=start;
    while(trav->next!=NULL)
        trav=trav->next;
    trav->next=ntemp;
}

void sll::insertafter()
{
    b:
    int key;
    cout<<"Enter PRN:- ";
    cin>>key;
    Node *trav=start;
    while(trav->PRN!=key && trav!=NULL)
        trav=trav->next;
    if(trav==NULL)
    {
        cout<<"PRN not Found "<<endl;
        goto b;
    }
    else
    {
        cout<<"Enter the details of member :-\n"<<endl;
        Node *ntemp=createnode();
        ntemp->next=trav->next;
        trav->next=ntemp;
    }
    
}

void sll::deleteatstart()
{
    Node *temp=start;
    start=start->next;
    temp->next=NULL;
    delete temp;
    cout<<"\nPresident Deleted"<<endl;

}

void sll::deleteatend()
{
    Node *trav=start,*prev;
    while(trav->next!=NULL)
    {
        prev=trav;
        trav=trav->next;
    }
    prev->next=NULL;
    delete trav;
    cout<<"\nSecretary Deleted"<<endl;
    }

void sll::deletemember()
{
    int key;
    cout<<"Enter PRN :- ";
    cin>>key;
    Node *trav=start;
    Node *prev;
    while(trav->PRN!=key && trav!=NULL)
    {
        prev=trav;
        trav=trav->next;
    }
    if(trav==NULL)
        cout<<"\nMember not Found "<<endl;
    else
    {
        prev->next=trav->next;
        trav->next=NULL;
        delete trav;
        cout<<"\nMember Deleted "<<endl;
    }
}

void sll::printtotal()
{
    if(start==NULL)
        cout<<"\nList is Empty "<<endl;
    else{
        Node *trav=start;
        int count;
        while(trav->next!=NULL)
        {   
            trav=trav->next;
            count++;
        }
        cout<<"Total Number of members are "<<count<<endl;
    }
}

void sll::concat(sll l)
{
    
    if(start==NULL)
        start=l.start;
    else{
        Node *trav=start;
        while(trav->next!=NULL)
            trav=trav->next;
        trav->next=l.start;
    }
    cout<<"\nAfter Concatnation :- "<<endl;
    display();
}





//========================Main Function============================//
int main()
{
    sll list1,list2,*l;
    int chL,chM;
    select_list:
    cout<<"==============Pinnacle Club=============="<<endl;
    cout<<"\nSelect List \n1.List1\n2.List2\nEnter Chooice :- ";
    cin>>chL;
    if(chL==1)
        l=&list1;
    else if(chL==2)
        l=&list2;
    else
    {
        cout<<"\nEnter valid list number ";
        goto select_list;
    }

    do
    {
        cout<<"\n1.Create \n2.Insert President \n3.Insert  Secretary \n4.Insert after member \n5.Display list \n6.Delete president \n7.Delete secretary \n8.Delete Member \n9.Find Total no. of Member \n10.reselect list \n11.combine list \n0.Exit \nEnter your choice :- ";
        cin>>chM;
        switch(chM)
        {
            case 1:
                l->create();
                break;
            case 2:
                l->insertatbeginning();
                break;
            case 3:
                l->insertatend();
                break;
            case 4:
                l->insertafter();
                break;
            case 5:
                l->display();
                break;
            case 6:
                l->deleteatstart();
                break;
            case 7:
                l->deleteatend();
                break;
            case 8:
                l->deletemember();
                break;
            case 9:
                l->printtotal();
            case 10:
                goto select_list;
                break;
            case 11:
                list1.concat(list2);
                break;
        }
    }while(chM!=0);
    return 0;
}