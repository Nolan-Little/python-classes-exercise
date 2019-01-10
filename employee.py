# Instructions
# Create a class that contains information about employees
# of a company and define methods to get/set employee name,
# job title, and start date.

# Copy this Company class into your module.

# class Company(object):
#     """This represents a company in which people work"""

#     def __init__(self, company_name, date_founded):
#         self.company_name = company_name
#         self.date_founded = date_founded

#     def get_company_name(self):
#         """Returns the name of the company"""

#         return self.company_name

#     # Add the remaining methods to fill the requirements above
# Consider the concept of aggregation,
# and modify the Company class so that you assign employees to a company.

# Create a company, and three employees,
# and then assign the employees to the company.


class Employee:
    """This represents an employee that works at a company"""
    def __init__(self, full_name, job_title, start_date, company_instance):
        self.full_name = full_name
        self.job_title = job_title
        self.start_date = start_date
        self.company = company_instance

    def set_job_title(self, job_title):
        self.job_title = job_title

    def set_full_name(self, full_name):
        self.full_name = full_name

    def set_start_date(self, start_date):
        self.start_date = start_date


    def get_full_name(self):
        return self.full_name

    def get_job_title(self):
        return self.job_title

    def get_start_date(self):
        return self.start_date

class Company:
    """This represents a company in which people work"""

    def __init__(self, company_name, date_founded, employee_list):
        self.company_name = company_name
        self.date_founded = date_founded
        self.employee_list = employee_list

    def set_company_name(self):
        self.company_name = company_name

    def set_date_founded(self):
        self.date_founded = date_founded

    def hire_employee(self, employee_instance):
        self.employee_list.append(employee_instance)

    def fire_employee(self, employee_instance_name):
       for employee in self.employee_list:
           if employee.full_name == employee_instance_name:
            self.employee_list.remove(employee)



    def get_company_name(self):
        """Returns the name of the company"""

        return self.company_name

    def get_date_founded(self):
        """Returns the date the company was founded"""

        return self.date_founded

    def get_employee_list(self):
        """Returns a list of all employees"""
        for employee in self.employee_list:
            print(f"\n{employee.full_name}, {employee.job_title}")


MyPlace = Company("MyPlace", "01/09/2019",[])

MyPlace.hire_employee(Employee("George", "Administrator", "01/10/2019", MyPlace))
MyPlace.hire_employee(Employee("Laney", "Administrator's Assistant", "01/10/2019", MyPlace))
MyPlace.hire_employee(Employee("Bev", "Administrator Assistant's Assistant", "01/10/2019", MyPlace))

MyPlace.fire_employee("George")

MyPlace.employee_list[0].set_job_title("Administrator")
# print(MyPlace.employee_list[0].get_job_title())


MyPlace.get_employee_list()

print(vars(MyPlace.employee_list[0].company))
