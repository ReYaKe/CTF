def dna_to_ascii(dna_sequence):
	binary_map = {'A': '00', 'C': '01', 'G': '10', 'T': '11'} #This mapping creates TFC as first characters
	ascii_text = ''

	for i in range(0, len(dna_sequence), 4): #Take chunks of 4
		binary_str = ''.join([binary_map[base] for base in dna_sequence[i:i + 4]]) #Create Binary string
		ascii_char = chr(int(binary_str, 2)) #Convert Binary into ascii
		ascii_text += ascii_char #combine ascii

	return ascii_text


dna_sequence = "CCCA CACG CAAT CAAT CCCA CACG CTGT ATAC CCTT CTCT ATAC CGTA CGTA CCTT CGCT ATAT CTCA CCTT CTCA CGGA ATAC CTAT CCTT ATCA CTAT CCTT ATCA CCTT CTCA ATCA CTCA CTCA ATAA ATAA CCTT CCCG ATAT CTAG CTGC CCTT CTAT ATAA ATAA CGTG CTTC"
dna_sequence = dna_sequence.replace(' ', '')
ascii_text = dna_to_ascii(dna_sequence)
print(ascii_text)
