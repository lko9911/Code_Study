// 배열의 정의
// 정적 배열 - 스택 메모리 영역에 할당
int a[n];

// C언어에서의 동적 배열 - 힙 영역에 할당 (유지)
int* a = (int*)malloc(n*sizeof(int));

// C++언어에서의 동적 배열
int* a = new int[n];


