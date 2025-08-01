# Student Attendence Record if 
from pyutils.colors import Colors

def check_record(s: str) -> bool:
        absence_count = 0
        leave_count = 0

        for day in s:
            if day == 'A':
                leave_count = 0
                absence_count += 1
            elif day == 'L':
                leave_count += 1
            else:
                leave_count = 0

            if absence_count > 1 or leave_count > 2:
                return False

        return True


inputs = (("PPALLP", True), ("PPALLL", False), ("P", True), ("A", True), ("ALL", True), ("LLALLPLLPLL", True), ("LLALLL", False))


for i in inputs:
    if i[1] == check_record(i[0]):
        print(f"{Colors.GREEN}PASS{Colors.RESET}")
    else:
        print(f"\n{Colors.RED}FAIL{Colors.RESET}\nfor {i[0]}\n")

