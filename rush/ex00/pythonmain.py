from typing import List, Dict

class Farmlove:
    def __init__(self, name: str, date: str, task_type: str):
        self.name = name
        self.date = date
        self.task_type = task_type

class TaskManager:
    def __init__(self):
        self.tasks: List[Farmlove] = []
    
    def add_task(self, name: str, date: str, task_type: str):
        """เพิ่มงานใหม่"""
        new_task = Farmlove(name, date, task_type)
        self.tasks.append(new_task)
        print("เพิ่มงานสำเร็จ")
    
    def show_all_tasks(self):
        """แสดงรายการงานทั้งหมด"""
        if not self.tasks:
            print("ยังไม่มีงานในรายการ")
            return
        
        print("\nรายการงานทั้งหมด:")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task.date} – {task.name} ({task.task_type})")
    
    def delete_task(self, task_index: int):
        """ลบงานตามลำดับที่ระบุ"""
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f"ลบงาน: {removed_task.name} แล้ว")
        else:
            print("ลำดับงานไม่ถูกต้อง")
    
    def summarize_tasks(self):
        """สรุปจำนวนงานแต่ละประเภท"""
        if not self.tasks:
            print("ยังไม่มีงานในรายการ")
            return
        
        type_counts: Dict[str, int] = {}
        for task in self.tasks:
            type_counts[task.task_type] = type_counts.get(task.task_type, 0) + 1
        
        print("\nสรุปจำนวนงานแต่ละประเภท:")
        for task_type, count in type_counts.items():
            print(f"- {task_type}: {count} งาน")

def display_menu():
    """แสดงเมนูหลัก"""
    print("\n" + "="*40)
    print("Smart Farm Task Organizer")
    print("="*40)
    print("1. เพิ่มงานในฟาร์ม")
    print("2. แสดงรายการงานทั้งหมด")
    print("3. ลบงาน")
    print("4. สรุปจำนวนงานในแต่ละประเภท")
    print("5. ออกจากโปรแกรม")
    print("="*40)

def main():
    manager = TaskManager()
    
    while True:
        display_menu()
        choice = input("เลือกเมนู (1-5): ").strip()
        
        if choice == "1":
            name = input("ป้อนชื่องาน: ")
            date = input("ป้อนวันที่ (dd/mm/yyyy): ")
            task_type = input("ประเภทงาน (พืชผัก/ปลูกสัตว์/อื่นๆ): ")
            manager.add_task(name, date, task_type)
        
        elif choice == "2":
            manager.show_all_tasks()
        
        elif choice == "3":
            manager.show_all_tasks()
            if manager.tasks:
                try:
                    task_num = int(input("ลำดับของงานที่ต้องการลบ: "))
                    manager.delete_task(task_num)
                except ValueError:
                    print("กรุณาป้อนตัวเลขเท่านั้น")
        
        elif choice == "4":
            manager.summarize_tasks()
        
        elif choice == "5":
            print("\nขอบคุณที่ใช้โปรแกรม Smart Farm!")
            break
        
        else:
            print("กรุณาเลือกเมนู 1-5 เท่านั้น")

if __name__ == "__main__":
    main()
