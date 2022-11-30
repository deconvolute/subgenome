import os
import sys

bact=str(sys.argv[1])
b1=str(sys.argv[2])

dbpath=b1+"/"

#os.system("cut -d ' ' -f1 "+bact+" > bacteria.fa")

#os.system("cd-hit -i bacteria.fa -c 0.9 -o non-redundant.fa")
#os.system("grep '>' non-redundant.fa | sed 's/>//g' | sort > allseq.txt")

#os.system("blastp -query non-redundant.fa -db "+dbpath+"humandb -out humanblast_out -outfmt 6 -evalue 1e-5")

#os.system("cut -f1 humanblast_out | sort -u  > humanblast_out_sorted.txt")

#os.system("comm -23 allseq.txt humanblast_out_sorted.txt  | sort > nonhuman.txt")
 
#os.system("seqtk subseq bacteria.fa nonhuman.txt > g1.fa")

#os.system("blastp -query g1.fa -db "+dbpath+"antitargetsdb -out anti_out -outfmt 6 -evalue 0.005  -qcov_hsp_perc 30")

#os.system("cut -f1 anti_out | sort -u  > anti_out_sorted.txt")

#os.system("comm -23 nonhuman.txt anti_out_sorted.txt > nonhuman1.txt")
 
#os.system("seqtk subseq g1.fa nonhuman1.txt > g2.fa")

#os.system("blastp -query g2.fa -db "+dbpath+"degdb -out deg_out -outfmt 6 -evalue 1e-100")

#os.system("cut -f1 deg_out | sort -u  > deg_out_sorted.txt")

#os.system("seqtk subseq g2.fa deg_out_sorted.txt > essential_genes.fa")

#os.system("blastp -query essential_genes.fa -db "+dbpath+"vfdb -out vfdb_out -outfmt 6 -evalue 1e-100")

#os.system("cut -f1 vfdb_out | sort -u  > vfdb_out_sorted.txt")

#os.system("seqtk subseq essential_genes.fa vfdb_out_sorted.txt > vf_genes.fa")

os.system("blastp -query vf_genes.fa -db "+dbpath+"antires -out anti_res.out -outfmt 6 -evalue 1e-100")

os.system("cut -f1 anti_res.out  | sort -u  > anti_res_out_sorted.txt")

os.system("seqtk subseq vf_genes.fa anti_res_out_sorted.txt > antires_genes.fa")

os.system("blastp -query antires_genes.fa -db "+dbpath+"drugbankdb -out drugdb_out -outfmt 6 -evalue 1e-100")

os.system("cut -f1 drugdb_out  | sort -u  > drugdb_out_sorted.txt")

os.system("seqtk subseq antires_genes.fa drugdb_out_sorted.txt > drugtarget_proteins.fa")

os.system("comm -23 anti_res_out_sorted.txt drugdb_out_sorted.txt | sort > novel_proteins.txt")
