import pytest
from pages.sprintgrid_page import SprintGridPage
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestSprintGridApp():
    log = Utils.custom_logger()

# Create an instance of class
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.sp = SprintGridPage(self.driver, self.action)  # sp is an instance of SprintGridPage class
        self.ut = Utils()  # ut is an instance of Utils class

    """2. User can create new task by clicking Plus “+” button and filling the name of new task. The name is unique. User can’t create two tasks with the similar name. 
        The task is required field. User can’t create task without name. In this case validation message “The title is required” should appear."""

    def test_add_task(self):
        # click on add task button +
        self.sp.do_click(self.sp.ADD_TASK_BUTTON)
        # Give Task name in the input field
        self.sp.do_send_keys(self.sp.SEND_TASK_NAME, "Task 4")
        # double click on Add button to add the task
        self.sp.do_double_click(self.sp.ADD_OPTION_TASK)
        # click on close task button x
        self.sp.do_click(self.sp.CLOSE_TASK_BUTTON)
        assert self.sp.assert_element(self.sp.IS_TASK_DISPLAYED) == "Task 4", "Task has not added"

    """3.User can create new Date (column) by clicking Plus “+” button and filling the date (using datepicker or keyboard).
        The date is required. If the date can’t be parsed, validation message “Follow the format mm/dd/yyyy” should appear.
        The date field is unique as well. User can’t create columns with similar dates."""
    def test_add_date(self):
        # click on add date button +
        self.sp.do_click(self.sp.ADD_DATE_BUTTON)
        # //click on calender icon
        self.sp.do_click(self.sp.CALENDER_ICON)
        # //click on dates on the calender
        self.sp.do_click(self.sp.DATE_ON_CALENDER)
        # // click on Add (date Add option)
        self.sp.do_double_click(self.sp.ADD_OPTION_DATE)
        # click on close date button

    """4.User can assign statuses by clicking to the cell of the table. Then the table expends, 
        and the nearest input is autofocused and is getting active."""

    @pytest.mark.parametrize("status", [("To do"), ("In progress"), ("In Testing"), ("Blocked"), ("Done")])
    def test_status_assignment(self, status):
        # click on the cell of the status
        self.sp.do_click(self.sp.STATUS_CELL)
        # clear the status field
        self.sp.do_clear(self.sp.STATUS_FIELD)
        # enter the status
        self.sp.do_send_keys(self.sp.STATUS_FIELD, status)

    """# //7. User can remove rows by hovering over the task name and clicking to remove button (red cross)"""
    def test_remove_rows(self):
        # move to web element and hover over and click
        self.sp.do_move_to_element(self.sp.REMOVE_TASK_ROW)

    """# 8. User can remove columns by hovering over the date and clicking to remove button (red cross)"""
    def test_remove_columns(self):
        # move to web element and hover over and click
        self.sp.do_move_to_element(self.sp.REMOVE_DATE_COLUMN)






        """# 8. User can remove columns by hovering over the date and clicking to remove button (red cross)
        web_element_date = driver.find_element(By.XPATH, "(//mat-icon[@role='img'][normalize-space()='close'])[2]")
        act.move_to_element(web_element_date).perform()
        web_element_date.click()
        time.sleep(5)
        print("8th case done")"""









# -----------------------------------------------------------------------------------------------------------
"""self.lp.do_click(self.lp.ACCEPT_PROMT)
            self.lp.do_send_keys(self.lp.USERNAME_TXT, user)
            self.lp.do_send_keys(self.lp.PASSWORD_TXT, password)
            if user == "anushapandit123@gmail.com" and password == "j7qRhh-aB8ttkqi":
                self.lp.do_click(self.lp.REGISTER_BUTTON)
                self.log.info("Login Successful")
            else:
                self.lp.do_click(self.lp.REGISTER_BUTTON)
                self.lp.notification_message(self.lp.INVALID_NOTIFICATION)
                self.log.error("Login Failed")"""



