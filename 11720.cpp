#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int num, sum = 0;
	scanf("%d", &num);

	char arr[100];
	scanf("%s", &arr);
	for (int i = 0; i < num; i++) {
		sum += arr[i] - '0';
	}
	printf("%d", sum);

	return 0;
}