# mock_genome_generator

Use a directory of fasta files to generate modified shortened versions of the genomes. Specify the input directory, output directory, number of genomes to be made, mininum genome length and max genome length

The flaw of this function is that is entirely relient on the length of contigs in your input directory. Eg if you have a contig that is longer than the min length it will produce a genome of 1 contig. As a result the distribution of contigs is off.

They way to fix this would be to figure out a way to model the number and length of contigs from some real genomes with similar sizes to your specified range and then use those genomes to specify the lenght and numbers of contigs for the new genomes. I have thought about implementing this but have not done so at this ponit in time.
