# include <iostream>
# include <cstdio>
using namespace std;
int main()
{
    int i,n,item,f,loc;
    char V[10], adm_no[100];
    cout<<"Enter Virus Composition: ";
    gets(V);
    cout<<"Enter number of samples: ";
    cin>>n;
    cout<<"\nEnter all "<<n<<" samples: ";
    for (i = 0; i < n; i++)
    {
        gets(adm_no[i]);
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