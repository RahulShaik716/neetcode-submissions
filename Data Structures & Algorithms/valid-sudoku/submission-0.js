class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {
    let row = new Map(); 
    let col = new Map(); 
    let square = new Map(); 
    for(let i=0;i<9;i++)
    {
        for(let j=0;j<9;j++)
        {
            let value = board[i][j];
            if(value==".") continue; 

            let key = `${parseInt(i/3)}-${parseInt(j/3)}`;

            if((row.has(i)&&row.get(i).has(value))
            ||(col.has(j) && col.get(j).has(value))
            || (square.has(key) && square.get(key).has(value))
            )
            return false; 


            if(!row.has(i)) row.set(i,new Set());
            row.get(i).add(value)

            if(!col.has(j)) col.set(j,new Set());
            col.get(j).add(value)

            if(!square.has(key)) square.set(key,new Set())
            square.get(key).add(value)
        }
    }
         return true
    }
   
    }
