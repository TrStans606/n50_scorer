def n50_scorer(file_name):
        genome_size = 0
        with open(file_name, 'r') as read:
                for line in read:
                        if line[0] != '>':
                                for bp in line:
                                        genome_size += 1
        print(genome_size)

        with open(file_name, 'r') as read:
                contig_num = 0
                contig_size = 0
                sum = 0
                iter = 0
                lines = read.readlines()
                while sum <= genome_size/2:
                        #print(lines[iter][0])
                        if lines[iter][0] == '>':
                                sum += contig_size
                                contig_num += 1
                                if sum >= genome_size/2:
                                        print("genome size/2: ", genome_size/2, " sum: ", sum, " contig_size: ", contig_size, " contig_num: ", contig_num)
                                        return contig_size, contig_num
                                contig_size = 0
                        elif lines[iter][0] != '>':
                                for bp in lines[iter]:
                                        contig_size += 1
                        iter += 1

file_name = input('enter the name/file path for the .fa file you want to find the n50 score of ')
#file_name = "velvet_output/contigs.fa"
print(file_name)
contig_size, contig_num = n50_scorer(file_name)

print("The n50 score for this genome is ", contig_size, " from contig ", contig_num)
