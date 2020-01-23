You are given a DOM tree and have to find the table with the largest number of cells within it. A table is represented by the
For example, given an HTML document with the following contents within the
<h3 > Some test tables < /h3 >
<div >
<p > First table < /p >
   <table >
       <tr >
            <td > First < /td >
            <td > row < /td >
        </tr >
        <tr >
            <td > and</td>
            <td > second</td>
            <td > row</td>
        </tr >
        <tr >
            <td > and</td>
            <td > the</td>
            <td > third</td>
            <td > one</td>
        </tr >
    </table >
</div >
<p > Second table</p>
<table >
   <tr >
        <td > Not</td>
        <td > so</td>
    </tr >
    <tr >
        <td > many</td>
        <td > cells</td>
    </tr >
</table >

there are two tables in the DOM tree. The first table consists of nine cells and the second of four cells(as you can see below). Thus, the correct answer is 9.

Some test tables

Write a function:

that, given a DOM tree, returns the largest cell count of any single table. For example, given the document described above, it should return 9. If the DOM tree does not contain any tables, your function should return 0.

Assume that:
