import sys
import textwrap

input_file = sys.argv[1]
output_name = input_file.split('.')[0]
output_file = f'{output_name}.gen.h'
lines = []

def main():
    with open(input_file, 'rb') as file:
        file_data = file.read()
    
    array_name = f'{output_name}_data'
    size_name = f'{output_name}_size'
    hex_bytes = [f"0x{b:02x}" for b in file_data]
    wrapped = textwrap.fill(", ".join(hex_bytes), width=100)
    header_guard = f'{output_name}_GEN_H'.upper()
    header_content = f'''
#ifndef {header_guard}
#define {header_guard}
const unsigned char* {array_name} = {{
{wrapped}
}};

const unsigned long {size_name} = {len(file_data)};
#endif
'''
    
    with open(output_file, 'w') as file:
        file.write(header_content)

    print(f'Wrote {output_file} with {len(file_data)} bytes.')

if __name__ == '__main__':
    main()