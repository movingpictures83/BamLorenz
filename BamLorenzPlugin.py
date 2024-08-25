from blc.blc import bamlorenzcoverage
from plugins.BamLorenz.utils import main, sam_to_sorted_bam

import PyIO
import PyPluMA

class BamLorenzPlugin:
    def input(self, infile):
       self.parameters = PyIO.readParameters(infile)

    def run(self):
        pass

    def output(self, outputfile):
        input_file_sam = PyPluMA.prefix()+"/"+self.parameters["samfile"]
        input_file_bam = PyPluMA.prefix()+"/"+self.parameters["bamfile"]
        sam_to_sorted_bam(input_file_sam, input_file_bam)
        b = bamlorenzcoverage()
        idx, n = b.bam_file_to_idx(input_file_bam)
        lc = b.estimate_lorenz_curves(idx)
        for key in lc:
            print(str(key)+"\t"+str(lc[key]))
