# include <iostream>
# include <string>
using namespace std;
int main()
{
    int N,i,j,k;
    char V[10];
    string B[100];
    cout<<"Enter Virus Composition: ";
    cin>>V;
    cout<<"Enter number of samples: ";
    cin>>N;
    if(N>10)
    {
        cout<<"Number of samples should be less than 10.";

    }
    else if(N<0)
    {
        cout<<"Number of samples should be greater that 0. ";
    }
    cout<<"Enter all "<<N<<" samples: \n";
    for(i=0; i<N; i++)
    {
        cin>>B[i];
    }
    for (i = 0; i < N; i++)
    {
        string arr_i [10];
        for (j = 0; j < N; j++)
        {
            arr_i[j] = B[j];
        }
        cout<<"These are the first three elements: \n";
        if(i < 3)
        {
            cout<<arr_i;
        }
        else
        {
            break;
        }
    }
    return 0;
}