import random, shutil, os, glob
from pyfaidx import Fasta

def mock_genome_creator(num_mock_genomes=4000, min_len=20000, max_len=500000, infiles, outdir):

    # I do not know how to glob on an argument correctly. I imagine it would be something like what is below but I have not tested it yet
    # It might also require another argument that is the ending of the fasta files eg .faa, fna 
    infiles=glob.glob(infiles+'/*.fasta')
#    outdir="/mnt/scgc/simon/microg2p/analyses/JdF_analysis/analysis/GUNC/testing/mock_SAGs_from_1mbp_SAGs_passGUNC/"

    # delete previous fasta files
    for f in os.listdir(outdir):
        os.remove(os.path.join(outdir, f))

    counter=1

    while counter <=num_mock_genomes:
        tlen=0
        new_contigs=[]

        # select a random fasta file from the list of infiles
        SAG_file=random.choice(infiles)
        SAG=os.path.basename(SAG_file)

        # load fasta file into index
        contigs=Fasta(SAG_file, key_function = lambda x: x.split('.')[0])

        #  pick a random number within the range previously determined
        genome_len=random.randint(min_len, max_len)

        #If the length is <genome_len repeat until it is >genome_len
        while tlen <=genome_len:
            # select a random contig from the list
            x=random.choice(list(contigs.keys()))
            #extract the name of the contig
            name=contigs[x][1:len(x)].name
            #check if contig is not in list of contigs
            if name not in new_contigs:
                #if the contig is not in the list add it to the list
                new_contigs.append(name)
                #and add the length of that contig to tlen
                tlen=tlen+len(contigs[x])

        # create a file with all the contigs that will make up the mock genome
        file=open('mock_contigs.txt','w')
        for items in new_contigs:
            file.writelines(items+'\n')
        file.close()

        #name of outfile
        outfile=outdir+'mock_gneome_'+str(counter)+"_"+SAG

        #generate the mock genome
        !seqkit grep -f mock_contigs.txt $SAG_file -o $outfile

        # increase the counter
        counter+=1
    print('done')
    
    
