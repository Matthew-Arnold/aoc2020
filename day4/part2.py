import sys
import re

def valid_byr(byr):
    return re.fullmatch(r'\d{4}', byr) and (1920 <= int(byr) <= 2002)

def valid_iyr(iyr):
    return re.fullmatch(r'\d{4}', iyr) and (2010 <= int(iyr) <= 2020)

def valid_eyr(eyr):
    return re.fullmatch(r'\d{4}', eyr) and (2020 <= int(eyr) <= 2030)

def valid_hgt(hgt):
    if not re.fullmatch(r'\d+(cm|in)', hgt):
        return False
    
    if hgt[-2::] == 'cm':
        return 150 <= int(hgt[:-2]) <= 193
    else:
        return 59 <= int(hgt[:-2:]) <= 76

def valid_hcl(hcl):
    return re.fullmatch(r'#[0-9a-f]{6}', hcl)

def valid_ecl(ecl):
    return ecl in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

def valid_pid(pid):
    return re.fullmatch(r'\d{9}', pid)

def valid_passport(passport):
    expected_fields = {'byr': valid_byr,
                       'iyr': valid_iyr,
                       'eyr': valid_eyr,
                       'hgt': valid_hgt,
                       'hcl': valid_hcl,
                       'ecl': valid_ecl,
                       'pid': valid_pid}
    
    
    return all(field in passport and valid(passport[field]) for field, valid in expected_fields.items())


if __name__ == '__main__':
    passports = []
    cur_passport = {}

    for line in sys.stdin:
        if line == '\n':
            passports.append(cur_passport)
            cur_passport = {}
        else:
            pairs = line.split()
            for pair in [p.split(':') for p in pairs]:
                cur_passport[pair[0]] = pair[1] 
    #handle the last one yolo
    passports.append(cur_passport)

    print(sum(1 for passport in passports if valid_passport(passport)))
