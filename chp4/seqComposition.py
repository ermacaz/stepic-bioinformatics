def seqComposition(text, k):
    kmers = []
    for i in range(len(text)-k+1):
        kmer = text[i:i+k]
        kmers.append(kmer)
    kmers.sort()
    f = open('seqcomp_output.txt', 'w')
    for kmer in kmers:
        f.write(kmer + '\n')
    f.close()

    return
    
seqComposition('ACAGGGCGCGGTTTTCAAGAACCTAAAGGGTCGACAAGGCCCCTTGCCAAGACTATAGTCTCTCACGTCGTTTGCTAATTTTTTACCCTTAGAGGTCTGAGTTCAGGGTTACTTCCAGTCCCCGTCTTCGTTATACTACCCGCAGCGTTAACACGCCAACTATCGACCCACTGCTGCCTGAGACATCCAGCTCCCTCGGGGTCCTCCGGTTTGGTATTGGTATCGGTGCCACCCGCCATTTGGCCGTGCCCCCTAAGCCCGAAAGCTACTTTCTCAATTAAGGCCATACAAAGCCTTTCGGGTCCCCCTCCAGCCTCCTCTCTGATATTGCATTTGCTACAGGGCTAAGAGTAAGGTTCGAGTAAATTGCGGTCATATCGTGATCCGACCTGAGGCTCACGGCAGGACGTACCACGCGAAAACGGGATTCCGGCGCCGTGACATGCTCGAGAGGATGAGTAGCATCTTATGTAAAGACGAGTCCGATACGGTCGCGTCCTACGATTCCCCCAGATTAGATTGTCCCCAATCAGACAGGACATCGCGTGTCTAGGCGACAGGCTGCCGCAGATAATGCAAGTGACTCGGGTGAGATGGTGCGATTCCGGAGGAGTAATCGCACACTGCAAGGGTGCTTCCCTTTCCCCTTATTGGTAGAGCAATCGTCAAGAACATATCTGTCGCCCCATAGCCTTCAAGATTCGGGTAAGAGTCGAAGACGCACCCCGCGCGCGAACCCCAAGCCTGAGCGACCCCCTCTCAGTTGACGTTAGGTGTAAGAGGCAGGATCATATCAATTACGCACGAAAACCCGTATCACGATGCAACGCCACGAATGACCAAAGCCATTGGTGAGGGGTCCTCATGTAATAAGAGCCCCAGCCGACTCATACAATTCATGGGGGTAACAGCGACCACGCACCGTCTGTTTCTCTAGGCGTGAGGGGCACTCCGTTCGCCACCATTGTCGTCGGCTAATAAGGAATTATGCCCGCTATCGTCCACGCACATTGACTACCGGCGTGAAGCCAACCCTCGTGACCCCAGTTCTGTAGAGTCGGCTACTGCTTTGTCAAGTTAAATTCTTAGGTACTACGCGATTACTATTTGAAGTTATCCTAGGACACATCTATCCCGTTCATATGTGTATGGCCACGACAACGATGGCGCGTTCACGCCAATTCACTTCAGCGAGTCATGAAAAGATGCTAACCGTAGACCTTGTGGCTACGGCGTGTCTCTCAGAGTGTCATATGAGGTGGAACCTCCTAGATTGTTTTTGCGGTAGTGATCCAGATACGCGGGGTCCCGCAGCATTAGTAAAATAGATCAATATTTTTCTATGGTAATCCAAGCTGCACTCTCAATCCGTGTGCTGATCTCAGAAGGCGATAGATAACAAGCGCAGTCGGACGACTAAGGGAGACTATCCTGACCTGGATTCTCCTCCATTAGATCTTGATATCGTTACAGGAATCGATTAATCAATAGCGAGGGAGCTATATAATTAAACATTCCGCTAAGCCCTTTTCTCTCCCACAGGGCCACGGATTGGTAGACAAATTAGTTGCGATTGATGGATCGACTCATTGACTGCTGTAGGGCGGGTGGTAAACATGTCTGGTGCTTGTTCGGTTAGATCCGCTCTACAAGATGCATACTATACGGTAGCTTTGGCGAGGAAGTCATACGCTTGTGAAGGAAATGCCCCAGAAGGCATCCACGTTAGTGTGCGGATCCGTTCCCTTCTAATACAAGAACCGCGAAAAATACTTGTAATCTAAGAAACATATTGGCTGCTACGAGAAGCGCACGTGGTCGGCGAGGGCCCTGGGAGACTTGACGACCCGTTCGTAGCGGCTCGTTAACAGCTGCTGGTCGCAACGATATTAGACCCAGTTAGTTGTGGATCACGAAATCTACTCTCAAGGAGTGCATTCGGCGCGAGGTGATGAAAGGCGCGCTCCAATGAATCGCAAGACTCATCCCGCAGCGGAGCTGTGACAATGCTACCGTTTGTGCTAGTGCTGTACTCGACTACGAGTACGACCTGTTTCGATGAAGGCCTCGCCCGTGCACTAACGTTTGAGAGAGCGAAATTACTCCACCTTGCACCCTTGTCGAGGTTGTACGAGCCTGTCATACTGAGTCCAAAAGATTTAGTCATCTAATTGTATCTCCATGTTTCTAGAGAAGACATGTGAGGGGCAGATCAGGTAAGCTGGGTCCGGCGGCATATCCTATAGGTCCGGGCAAGGCGTCAGGCAAAATACTACGAGCATCTTAGAAATAGGGCTATGTATGCTTATCTTATACTGACCGTGCTTAATACACTTAATCGATATCTGTTGGACGTCTCGGGTCTAAACACATATACTCTTAAGAGGGATTCGTATGTTCCCGAGAAACGTAGTCCCGGAGCTATGGATGGCCGGTCCAAGTGGAGAGTTCTCTCAGGGGGGTTATGGTGTTTGTTGGACCCACCGTCTCGTTGGTCCATTAATTCGAAAGCCAGGCCGGGAACAAGGGAACATGGTGTTCGCCCGGGGTTTCACCTTCCAACCGATTCGAAACAAGTTCAGGAAAAATAGTGCCCCTGCCGATATCTCAGTATCCAAAATGAGGAGCGTGTTGGGTGTGCGGCAACTAGTTTGTAGAGTGACATTTAAACTTTCAGAACATGGTTTTTGATGTCCTGGGTTGGTATTGATTTCCCCTGGTAGTGGAGTATTGGATGACCCTGGGTTTCGCAGATACGATATCCCAGGTAATGGAAATCCAGGCCTATGGGAGATGCCTTTTCCCTATGAAAGCGCGTATATAGTAAATAACTGCAACGCTAGTTCGGGCGCGGATAGTCGGTCTAGCACGCCAGTTGCTGTTTAACTGCGGCAGCGTTTCTGCAGTTGTCGCTCGACCGAGGTAAACGAACAATAGTTCTGCTGTCGTAGTGTCTAAGAGTCCTCCGTACGGCCCGGTCCAGGGGACTCAGGCGAAGAGCTCCAACACGGAGGTGAAGCATTGCAGTCTTACTACGTACTCAAAACCTTATTTTTACCAAGGCGCAAGTTATTGTAAGAGCTGATGAAATTGCTTGCAGAAGATTAGTTATCAGTTTCCGTCTTCAGACGTTGTATACAAATGTGCGAATAGGTGGCGGTCGCTCCTACCCCCGCCAACGTGGCGAGCTCGACAGCATACTCGGTTCGTGAGCCCTACCCGCCGTGCCACACGACTTAAGGTTGAGGCGGCAATACTAGAAAGCTAGGTGATTGGGAGTGACATAGTTGCTCACCATAACTTTGCAAGGCAGGATCTGGAACAAACACGCGCCGATCCGACGCGATACTAATAGTGCGGTCCAGAATGCTTTCCATTTCTGCGCAAATGTTGCACTGCTCTGTTTCACCGCTCTACCCATTTCACAGCCCAGATAAGCGTACGACAGTATATGAATCTACCCCGGGCACACTAAGCGGTTCAGAGATGTGATATGGATTCCATGCTAGCGAGCGAGAACACCGCATCGCTCAACCCCTTGGTCACACTGTTCAAACAGTTATTGCCATTATATCCCACACCAGTCGCCAGCCCCCCAATCTGCGGTGAACCATTACACTCGCCCGCAGACTAATACGCGTCAATTAAATGTATTTAGACCCAAAAAAGCGATCATATCCGTTCGCCTGGTTCTGATGGCGCTTTCGCGAAAGGATAGACGTTTGCAGATGTAGGGTGCTAACTGTACCCTCTCAAACCGGAATATTTAGTTGGTTATAAGCGCTCGCCGTTTTATCGGCTACGTAAAGAAGCCCTAAAATCAAGCCGCTCAAGTTTTGCAAGAAGATGCCGCAGATAAGCTCGTGCCTCCGAAGAGGATAAACCTGCCGCAAGTTGAGTGGGGATTTGACGAGAGGGGCGGGTATGAGGCGAGAAGGTGCATAGTCTTAGTTTTCCAATACTGCGGAACATGCCGAGCAGCCCAGATAACAGTAGAGACTACGAACGAACTTTTATCGACCTATAAGAGGTGCGTTCTCACATGAAGGCCCTCACAATCGTGTGTGACCCCACGGTCTTGCCAACCAAATGGTCATAACGGCTTCCCGCTGCTCGCCGGTATTCTATTCAGAACAAGGACTCTATCATCTGATGGCGGCGCTAACCTATAGCAGGGTTGTACAGTAAACGTCCGAGAAGTTGCATAGGCACTCCTTCAACCCGACTTGCAGATATGAACTAGTGGGGCTGTGTGATGTACAGACGCATATTGTGACCGACAGTTTAGGGGCGAATAAGTCGGGGCTTCTTATCCGTACGACTGGCAAACAACAAGTCCCGTTGGCCCAAACCCAGTCTGTACTGCCTCTATATACCATACTTCAGTCGCTGTTACACCACCAATGGCAACGAAGTGTTCGCAGCGGCACATTTAGTGCTTCACGGGACCCCTCGCGCTGTGGACACAAGGCGCGATCACCCGGAACCAACAGAATCTGTGACTTGTACTTATCAAAGGAAGCAATAGCGGTGCCAGGCGCAAGTGCCTCTTGACTACCAGTCTCATTATGCTCGGAGTAAGAGATCGGGACGCAGCCTTGCGCAACGATCGGCGCTTTTTGGCCCTCTAGCTAATGGGGCAGTGCCATTATCTAGTAATGAATACTATCGCTCACTCTATATGGTGGCTATGAGTTGTTTATAACTGCGGGAGGCGCGGATGAGCATCTCGTTTATTGAAGATAAACGATAAGGATTCGTAGCTATTGAGGTAGTTCCAATTTTCCCGTAAGTAGAGTGTCACGCGTTAGATGCTAAGATCCAACACCCGATTTAGACTAGAGCGGCCTTATGGGAAGACCCTGTCGCCTAAACCGAGCCAGGTCGGTATATGTTGCCCGACGTCGGGGATATAATGGTACCAACGCATCTACCATCACCCTCATCACCATGGGTTGCCGGCGTGGATATCCCGACCCAATACATGAGTGACAGGGTTCCACCAAACAAAATAGCGTTTGCCCCTAACATGTTGCGTTTTGCTGGACCACTTGTTGGTCAGAGTTCAACTAGCAGGAAGTGCTTCTCCGCAGGTCGCGTGTAAGTCAGCATTCTACGGTATCATGTTGGAATGTGGTGAGCGTGGGCCGACGTCGGCAGAGGGGATTCTGTAGTCTCGACCTGCAACCACCTACCCCGGTTGGAATCACATCACTTGATTGCGATCGACTGGGGCTACTCCGATTCCGATCAGCTCTTTATTGGACTGAACGCACTCCGCTGCCAGGTGGCGGGAGAACTCATACTGGGACCGAATAAACTCCGCTATGGAACAAAGACCGACACGTAGACAGTCCCCCAAGTGTGCCATGCTTGGCGAATGGACACTCTATAGACGAATATGCCGTCCGTCTTATTTTTATTGAGCGTTGCCTAGCCTGGTCATCCATACGCGGACGTGTCCACCCTGAAACTAGCCAGAATCCACTCGCCTTGCAATGACTGGTTCTTAGTCAAGAAGACATACTCGTTTCGGCCGTAATTACCCGATGGAAGACCTTTGGTGGGGTAGATACGGTTCGCTATTGAGACCATCAGCGATCCTAAATGATTTACTGACCGGATCGCCCGGCAAGGCAGACAATATCCGACCAATCTCGCAGTAGGGGGTCTGACCCAGCCGATCTGGCAGCCGTATCCATGCATAGGGCTCCCTAGAAGTGCGCTCTTAGGCTATCTGTGCCCTGTGGGTGGAACAGCCCACAAAGTCTAGCGCAGGGTACCTCAAACTGTGGAGGCGGGAGCTGTACCAGCATGGATGATTGATACACCACCTAACGCGACAAACCTTCTTGCTATACATGTCGTGCTCAGCGTTGATAAAAGAACGCAACCAACCATGCGTCTAGAATGTGAAGTAGGAGCGTCATTGTTTCCCACCGGTTCCCCTAGCTCAGTAAGGGGAGAGTAGCCGACGGTTCCCTGTATACGGCAAATTACGTGTGGGGTTCGTGCACAACTGACGCGCAGAAGGGAGACTCACGTATACTCGGTTATCAATGGTTTTAAGATCAGCATATCTTTTTGCATGCTTTGTACCAATACGCTTCGGAATCTTCCGGTGGCACCTTTAATCAGGGTGGAGCCGATACGACCTGTGCCAATGGGACACTCCACCACAGTACGATGAAAGGTCGAGAAAAGAGTCCCGGTTATGACCCCCCTTTGATCTGCCCTACAATTCTTTTTCTTTAGACGACAGTTGATACCATTTCAATGTCCTGAAACTGCAAAGACGCCGCCGGGAATGCATCTCCTTCACCATGACAGGGGACAAACCGATACAGTTTCCGGGACCCATTTCCGTACCCACTGTGAATCATCGCCGCCTTAGCTTGTTGTTACTAGATTATCAACCGGCTCGCAGGGCTTTCGAATGAAAACACATGATCGCGCCTCAGTAAAGCGGAAATATTTACTGACTCGAAGAACTGTGCATCTAGAAAATTAGGACATGAGGGTCGGCGGGGGTCGACCGGAGACTTACTCCGCGACAAATTTCAAAGTCAACTCTGCGGTGTTCGTGAGAGCTAGAGAAGCATGTTCCATGATGGAAAATGTGAATAGCCGGTGACAGCCTTTCGGAAAGCATTCGGTGATCCGTCGTAGGAGTCTCCGTCCACTGCGATATGGCATTGTCGTGTGGCCGGCATCCTGTCGAGCAATGTGGATCCCGAATGACTCGTACACTTGTAGGACGGCACGGCAAACGGCCAACTTCGGTTACAGTAGACCATAGCCGTCAATTCCTTTAGTTTGGCCAGACATACGCCGACTCCCTTTTGTCCATAACCTCATAGTCCTCAAGTTTATCGTACATCGCATCAGCCTATACATATGTAACCTAAATATGAGTGTGACTGCGGAAAAGCCTCCGTGGCGTTCGTGACAGCAAAATGGTCTTGACACGTTCAAGGGCCGTACAATGCGCATAATCAAATAACTCCGTCGCAGCTGGGAAATACTAGTTGAACATTGATAAGATCAAGGGTTTTTGTTGGTTGAGATCAGCGCAGACCCGGAATTGTGTAGATTCTGAGGGCATCTCGCATCTACCCGTCATGGCCAGTTGCCGGCCCATCCTCTAGGTTCTGTGGTCAGATACGAAGCACGTTACTCGCCTTTGGAATGCCCTGAGAGAGTGTTCGGCCCACTGATAGCGCAAGAGGATTACACAGGGGATAAATGAAAGCGCGGATTAATTACGTCTAGACGTAAGTCCCAGGTCGATTCTTGTACTATTTACAATCGGCTACTCAGCGTTGTTTCTGGCAAAGCGGGTGCACGAATGTAACAGAGCAACTCCAGACGAATCGTTCAGCGTTCGTATGCCCGAGAATGCGAACACGTAACCGAATTGTCTTAACCCCCACATCGCGGGGGTGTTAGGCCCGGTAACAAAGCCTACAGGCGCTCAGAACTAAGATGTCACGAAGCTCTAAGGTGTCATTGGATCACGACTCCACTACTTTGGACCAAGACTAGTACCTTAGAAACTTCTCGGGCTGGACGTATTTAAGCTTCTCCGCCAGGGGGGCGTTTTTTCCTAAAACCCACTGAAACCAAACACTGGCGTGAAGGTTCGACACCAGTCTTCCTGCAGTACACGCTAGCGCCCAGCATTCGAGGGCTGCGGCTCACCAGCTCGATTCAGGAAGCTCCTCCCGCGTCTGGGGGGTTACCCAGAGAGGTTCTGTTACCTAGGTACGTTCCATAATCTGAGTCCGCTCGGGGAGGCCAAATACCTGGACAATATATAGGCGAGTATTATGTGAACCCGAAATCTGATATCCAACAGAGGGAAAATCTCTCGTTGTCTCGTCGCCCTAGAAACATTACAATTCTGTGAGCGTAAACTACAATTCCCTACCCACTGAAGGTTGGTTATTCGTCGCTTGTCTACAGTTACCTCTGGTATTGCTCGTCGCCCCCATGCACGGCCTTGACCATTCGCCCACTATGGCGTAACCCCATCGCGAGAGACCAGTAAGAACAGGATAGCACCAACTATGTAGGACGTGGCAGAATCTGATCTAGCAGTGGCGGCGATGATCCATGGTCCAGTATCCCGTACTGTGAGCCAGGGGTTTGCATAATTGCTTTCGAGGAAACATCCTATTAATCGGGGTGCGCTTAGTTGCATCTATTGCTTTATATGATTGCAGGCACGGGTCATGTTCCGGTTCCAACTATACCACTGTCCCTAAACGACCTTGATTCCAGACGGCAGCTCTATCGTAATAAACGATACCACCGTTATAGTTAACGACATATCTCGCCTCGTATCGAGCTGACTTACCAGCCCCCCTCGGAGTGAGTCAAGGCCCTGAGGTAAGGCCGTTCGATTACCGACCTTGATGGAATTGGTTGTGGCATTTACTCGGGATCTGCTAAACGCGGGAGTGTCGGGGCATGTTTGTGCAATATTGCGTATCCGTGCCATCATTCAGAACACATGTGCTGTCCTTCTCATAAGAGCTCACTGTTATTGACTTTCGTGTGTTTGTGGAGAGTGTGAAGCCGCGATGGGGCATGTCTAACGACGCTATGCCAGTTAGAGAGTGATTGCGTGACCAACTGCACACCGCCGGGATTGGGTACACAGTCTAGTTATTAGGGCTCCTTTTAGCCCAATGCAAGGAACCGGTTGAGGATTTAAGTCAGGTTGCCGACGATAGAAATCGCCAACAAAACGTCCCTGTAGGGTTTCGACGCGATGAGATATCGTGAGACGGCACTGCACCCCCTTCTTCACATATTTATAACACCACCAATCGAGGCCAGTGCCCCATGCCGTTCTTAGCGATCTCGAAGGTTATACTACACCATGTTTGTACCTCACAATCTCGTCAGTGGAGCAGCAGACTTGCCGGCTCTATTCCCCGTATACAGTCGTAAAAACGAAGAGGCTGAACTATATATGAGATTGCAGTTACGACAGGAAGTAAATGACGCTAATGTACTCGAGCTGGACATAGACACCTAGCCGAGAGGGGCTATCTTGCTCCAAATGTGTTTATAGGCGACGTTGACTGGTAAAGCACTTTGGAGGGGAATGGCCTCAGATAATAGTAGTTAGCGCGCCGGCCCGCCGAGCACGACAACAGACAACTTAGTTCTATGGACGGTTGATTATCATATACGTAATGCCGACATACGCCGATTACCAATATTGCACTTATCTAAGAAAACGCAACCTAATAGCATGGTGGGCCGTCACTGTCTCGCGCACAGGCTCGATTTAGT', 100)