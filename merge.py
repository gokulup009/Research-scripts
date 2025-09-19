def parse_frame(lines):
    """Extract timestep, box bounds, header, and atoms from frame lines."""
    timestep = int(lines[1])
    num_atoms = int(lines[3])
    box_bounds = lines[5:8]
    header = lines[8]
    atoms = lines[9:9 + num_atoms]
    return timestep, box_bounds, header, atoms

def update_atoms(atom_lines, new_type, id_offset, type_limit=1400):
    """Change type to `new_type` if in range [1, type_limit], and shift ID."""
    updated = []
    for line in atom_lines:
        parts = line.strip().split()
        parts[0] = str(int(parts[0]) + id_offset)  # shift atom ID
        old_type = int(parts[1])
        if 1 <= old_type <= type_limit:
            parts[1] = str(new_type)               # override type only if in range
        updated.append(" ".join(parts))
    return updated

file1 = "dump_101.xyz"
file2 = "dump_102.xyz"
output_file = "merged_101_102.xyz"

with open(file1) as f1, open(file2) as f2, open(output_file, "w") as out:
    while True:
        # Read one frame from file1
        header1 = [f1.readline() for _ in range(9)]
        if not header1[0]: break  # EOF
        num_atoms1 = int(header1[3])
        atoms1 = [f1.readline() for _ in range(num_atoms1)]
        timestep1, box1, atom_header, parsed_atoms1 = parse_frame(header1 + atoms1)

        # Read one frame from file2
        header2 = [f2.readline() for _ in range(9)]
        num_atoms2 = int(header2[3])
        atoms2 = [f2.readline() for _ in range(num_atoms2)]
        _, _, _, parsed_atoms2 = parse_frame(header2 + atoms2)

        # Modify atoms
        modified_atoms1 = update_atoms(parsed_atoms1, new_type=1, id_offset=0)
        modified_atoms2 = update_atoms(parsed_atoms2, new_type=2, id_offset=17000)

        # Write merged frame
        out.write("ITEM: TIMESTEP\n")
        out.write(f"{timestep1}\n")
        out.write("ITEM: NUMBER OF ATOMS\n")
        out.write(f"{len(modified_atoms1) + len(modified_atoms2)}\n")
        out.write("ITEM: BOX BOUNDS pp pp pp\n")
        out.writelines(box1)
        out.write(atom_header)
        out.writelines(line + "\n" for line in modified_atoms1 + modified_atoms2)

print(f"✅ Merged file written to {output_file}")

