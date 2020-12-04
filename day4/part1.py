import sys

if __name__ == '__main__':
    expected_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
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

    print(sum(1 for passport in passports if all(field in passport for field in expected_fields)))