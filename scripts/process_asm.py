import idautils
import idaapi
import idc
import re
import json

loc_pattern = re.compile(r' (loc|locret)_(\w+)')
self_pattern = re.compile(r'\$\+(\w+)')

def rebase(asm_dict):
    index = 1
    rebase_assembly = {}

    addrs = list(sorted(list(asm_dict.keys())))

    for addr in addrs:
        inst = asm_dict[addr]
        if inst.startswith('j'):
            loc = loc_pattern.findall(inst)
            for prefix, target_addr in loc:
                try:
                    target_instr_idx = addrs.index(int(target_addr, 16)) + 1
                except Exception:
                    continue
                asm_dict[addr] = asm_dict[addr].replace(
                    f' {prefix}_{target_addr}', f' INSTR{target_instr_idx}')
            self_m = self_pattern.findall(inst)
            for offset in self_m:
                target_instr_addr = addr + int(offset, 16)
                try:
                    target_instr_idx = addrs.index(target_instr_addr)
                    asm_dict[addr] = asm_dict[addr].replace(
                        f'$+{offset}', f'INSTR{target_instr_idx}')
                except:
                    continue
        rebase_assembly[str(index)] = asm_dict[addr]
        index += 1

    return rebase_assembly

def get_assembly_by_ea(ea):
    instGenerator = idautils.FuncItems(ea)
    raw_assembly = {}
    for inst in instGenerator:
        raw_assembly[inst] = idc.GetDisasm(inst)
        
    rebased_assembly = rebase(raw_assembly) 
    return rebased_assembly

if __name__ == '__main__':
    binary_abs_path = idc.get_input_file_path()
    output_path = binary_abs_path + '.json'
    function_list = idautils.Functions()
    result = []
    for func_ea in function_list:
        function_data = get_assembly_by_ea(func_ea)
        result.append(function_data)
    json.dump(result, open(output_path, 'w'))
    idc.qexit(0)