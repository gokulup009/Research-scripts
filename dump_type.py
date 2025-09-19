input_file = "dump_10.xyz"      # Replace with your actual dump file
output_file = "processed_101.dump"

with open(input_file, 'r') as fin, open(output_file, 'w') as fout:
    num_atoms = 0
    read_atoms = False
    atom_lines_left = 0
    type_index = None

    for line in fin:
        if line.startswith("ITEM: NUMBER OF ATOMS"):
            fout.write(line)
            num_atoms = int(next(fin))
            fout.write(f"{num_atoms}\n")
            continue

        if line.startswith("ITEM: ATOMS"):
            fout.write(line)
            fields = line.strip().split()[2:]  # e.g., id type x y z
            type_index = fields.index("type")
            atom_lines_left = num_atoms
            read_atoms = True
            continue

        if read_atoms and atom_lines_left > 0:
            tokens = line.strip().split()
            atom_type = int(tokens[type_index])

            if atom_type <= 3200:
                tokens[type_index] = "1"
            elif atom_type == 3201:
                tokens[type_index] = "2"
            else:
                tokens[type_index] = "3"

            fout.write(" ".join(tokens) + "\n")
            atom_lines_left -= 1

            if atom_lines_left == 0:
                read_atoms = False
        else:
            fout.write(line)

