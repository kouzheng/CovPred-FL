import feature
import predic_fl

if __name__ == "__main__":
    fname=raw_input("Fasta file for surface protein:")
    pconf=float(raw_input("Cutoff value 0.0-0.5:"))
    feature.ft(fname)
    predic_fl.prfl(pconf)
    

