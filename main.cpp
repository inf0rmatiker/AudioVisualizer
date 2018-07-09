#include <iostream>
#include <vector>
#include "AudioVisualizer.h"

using namespace std;

int main() {
	cout << "======= TEST CODE BEGINS ==========" << endl;
	AudioVisualizer av(5);

	
	for (Band b : av.getBands()) {
		cout << "Band ID: " << b.getID() << "\n";
	}
	


	cout << "======= TEST CODE ENDS   ==========" << endl;
	return 0;
}