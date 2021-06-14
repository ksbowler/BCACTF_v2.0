#include <stdio.h>
#include <stdlib.h>

int main() {
	int money = 15,amt=10000;
	while (1) {
		int tmp;
		tmp = 100*amt;
		if(tmp < money) {
			printf("%d\n",amt);
			break;
		}
		amt++;
	}
	return 0;
}

