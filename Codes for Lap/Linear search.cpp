# include <iostream>
using namespace std;
int main()
{
    int adm_no[100],i,n,item,f,loc;
    cout<<"Enter number of students: ";
    cin>>n;
    cout<<"\nEnter admission number of "<<n<<" students: ";
    for (i = 0; i < n; i++)
    {
        cin>>adm_no[i];
    }
    cout<<"\nEnter the admission number to be searched: ";
    cin>>item;
    for (i = 0; i < n; i++)
    {
        if (adm_no[i] == item)
        {
            f=1;
            loc=i;
        }
        
    }
    if (f == 1)
    {
        cout<<"\nSearched successfully. Location = "<<loc+1<<"";
    }
    else
    {
        cout<<"\nSearch is failure";
    }
    
}