#include <iostream>
#include <string>
#include <vector>


class Band {
public:

	Band() : Band(0) {} // default ctor
	Band(int id) : bandID(id) {} // sets up Band ID
	~Band() = default; // default dtor

	int getID() { return bandID; } // getter for Band ID

private:
	int bandID; // Index number of band
};



class AudioVisualizer {
	public:

		AudioVisualizer() : AudioVisualizer(0) {}
		AudioVisualizer(int numBands) : numBands(numBands) { initializeBandVect(); }
		~AudioVisualizer() = default;

		int getNumBands() { return numBands; } // getter for number of bands
		std::vector<Band> & getBands() { return bands; } // getter for vector holding Band objects

		/* pushes Band objects onto Band vector	*/
		void initializeBandVect() {
			for (int i = 0; i < numBands; ++i) {
				Band band(i);
				bands.push_back(band);
			}
		}


	private:

		int numBands;
		std::vector<Band> bands;


};

