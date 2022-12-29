
const {Builder, By, Key} = require ("selenium-WebDriver");
const assert = require ("assert");

// create a function 
async function sprintgrid(){

//launch the browser
let driver = await new Builder().forBrowser("chrome").build();

//naviage to the application
await driver.get("http://localhost:4200/")


//2. User can create new task by clicking Plus “+” button and filling the name of new task.
//click on add task button +
await driver.findElement(By.xpath("//button[@aria-label='icon for open/close add form']//mat-icon[@role='img'][normalize-space()='add']")).click();
//Give Task name in the input field
await driver.findElement(By.id("mat-input-6")).sendKeys("Task 4");
//click on Add (Task Add option)
await driver.findElement(By.xpath("//button[@type='submit']")).click();


//3.User can create new Date (column) by clicking Plus “+” button and filling the date (using datepicker or keyboard).
//click on add date button +
await driver.findElement(By.xpath("//button[@aria-label='Icon for open/close add form']")).click();
//click on calender icon
await driver.findElement(By.xpath("//button[@aria-label='Open calendar']")).click();
//click on dates on the calender
await driver.findElement(By.xpath("//div[normalize-space()='30']")).click();
// click on Add (date Add option)
await driver.findElement(By.xpath("//button[@class='mat-focus-indicator date-form__add-button mat-button mat-button-base']")).click();


//4.User can assign statuses by clicking to the cell of the table. Then the table expends, and the nearest input is autofocused and is getting active.
await driver.findElement(By.id("mat-expansion-panel-header-4")).click();
await driver.findElement(By.id("mat-input-4")).clear();
await driver.findElement(By.id("mat-input-4")).sendKeys("To do");

//4)close the browser
await driver.quit();
}
sprintgrid()