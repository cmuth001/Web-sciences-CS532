#include <iostream>
using namespace std;

int main() {  
    int * nextPermutation = NULL;
    int n=0,k=-1,pivotValue=0,pivoteIndex=0,minIndex=0,temp=0,leftIndex=0,rightIndex=0,minValue=0;
    cout<<"Enter the Length of the array:";
    cin>>n;
    nextPermutation = new int [n];
    cout<<"N :"<<n<<endl;
    for(int i=0;i<n;i++){
        cin>>nextPermutation[i];
    }
    for (int i=n-1;i>=0;i--){
        if(nextPermutation[i-1]>nextPermutation[i]){
            
        }
        else{
           k=i-1;
           break;
        }
    }
    
    if(k!=-1){
        cout<<"--->pivotIndex: "<<k<<", pivotElement: "<<nextPermutation[k];
        pivotValue = nextPermutation[k];
        pivoteIndex = k;
        k=k+1;
        minValue = nextPermutation[k];
    
        for(int i=n-1;i>=0;i--){
            if(nextPermutation[i]>pivotValue){
                minValue = nextPermutation[i];
                minIndex = i;
                break;
                
            }
        }
        cout<<endl<<"minIndex:"<<minIndex<<", minValue: "<<minValue;
        //Swaping Elements
        temp = nextPermutation[pivoteIndex];
        nextPermutation[pivoteIndex] = nextPermutation[minIndex];
        nextPermutation[minIndex] = temp;
        for(int i=0;i<n;i++){
            cout<<nextPermutation[i]<<" ";

        }
        leftIndex = pivoteIndex+1;
        rightIndex = n-1;
        while(leftIndex<=rightIndex){
            temp = nextPermutation[leftIndex];
            nextPermutation[leftIndex] = nextPermutation[rightIndex];
            nextPermutation[rightIndex] = temp;
            leftIndex += 1;
            rightIndex -= 1;
        }
    }else{
        cout<<"This is the last sequence number in Permutation.";
    }
    cout<<endl;
    for(int i=0;i<n;i++){
        cout<<nextPermutation[i]<<" ";

    }
    return 0;
}
