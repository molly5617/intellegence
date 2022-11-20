#include<iostream>
#include<fstream>
#include<queue>
#include <tuple>
#include <cmath>
using namespace std;

struct point
{
    float x;
    float y;
    int index;
};
int rank[2001];
point ans[2001];
point temprank[2001];
int ranks[10000];
int maxrank=0;
int minrank=9999;
void maxheap(point ans[],int n,int i)
{
    int largest = i;
    int l = 2 * i + 1;
    int r = 2 * i + 2;
    
    if (l<n&&(ans[i].x< ans[l].x))
    {
        largest = l;
    }
    if(r <n && ans[largest].x <ans[r].x)  
    {
        largest = r;
    }
    if (largest != i)
    {
        point temp;
        temp=ans[i];
        ans[i]=ans[largest];
        ans[largest]=temp;
        maxheap(ans,n,largest);
    }
}

void heapsort(point ans[],int num)
{
    int n = num;
    
    for(int i=((n/2)-1);i>-1;i--)
    {
        maxheap(ans,n,i);
    }
    
    for(int i=n-1;i>0;i--)
    {
        point temp=ans[i];
        ans[i]=ans[0];
        ans[0]=temp;
        maxheap(ans,i,0);
    }
   
}

    
void findrank(int left, int right) {
	if (right - left <= 1)
		return;
	int middle = (left + right)/2;   
    int counts = 0;
    int i = left;
    int j = middle;
    int k = left;
	findrank(left, middle); 
    findrank(middle, right);
	while (i < middle || j < right) {
		if (i == middle) {
			temprank[k] = ans[j]; 
            ranks[temprank[k].index] += counts;
			j++; 
            k++;
		}
		else if (j == right) {
			temprank[k] = ans[i];
            k++;
			i++; 
		}
		else if (ans[i].y < ans[j].y) {
			temprank[k] = ans[i]; 
            counts++;
			i++; 
            k++;
		}
		else {
			temprank[k] = ans[j]; 
            ranks[temprank[k].index] += counts;
			j++; 
            k++;
		}
	}
	for (i = left; i < right; i++)
		ans[i] = temprank[i];
}
    




int main()
{
    int choose;
    int left,right,i=0;
    float b,c;
   
    ifstream myfile;  
    myfile.open("test2.txt");
    float sum = 0, value = 0;
    
    
    
    while(!myfile.eof())
    { 
        myfile >> b >> c;
        ans[i].x=b;
        ans[i].y=c;
        ans[i].index=i;
        i++;
    }

   
    int num=i;
    point temp[2001];
    for(int i=0;i<num;i++)
    {
        temp[i]=ans[i];
    }
    heapsort(ans,num);
    for(int i=0;i<num;i++)
    {
        cout<<"("<<ans[i].x<<","<<ans[i].y<<")"<<" ";
    }
    cout<<endl;
    findrank(0, num);
    int average=0;
    for(i=0;i<num;i++)
    {
        if(maxrank<ranks[i])
            maxrank=ranks[i];
        if(minrank>ranks[i])
            minrank=ranks[i];

         average=average+ranks[i];
    }
    
     for (int i = 0; i < num; i++)
			cout <<"("<<temp[i].x<<" , "<<temp[i].y<<")   "<<"rank="<<ranks[i] << '\n';
    cout<<"檔案中所有點的個數:"<<" "<<num<<endl;
    cout<<"最大rank:"<<" "<<maxrank<<endl;
    cout<<"最小rank:"<<" "<<minrank<<endl;
    cout<<"平均rank:"<<" ";printf("%.2f",(float)average/num);

}