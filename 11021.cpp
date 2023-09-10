#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {

	int i, a, b;
	int num;
	scanf("%d", &num);

	for (i = 1; i <= num; i++){
		scanf("%d %d", &a, &b);
		printf("Case #%d: %d\n", i, a + b);
	}

	return 0;
}