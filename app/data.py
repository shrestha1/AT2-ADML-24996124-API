state_store = {
    'CA' : [1, 2, 3, 4],
    'TX':[1, 2, 3],
    'WI':[1, 2, 3]
}

department = {'FOODS': [1, 2, 3], 'HOBBIES':[1, 2], 'HOUSEHOLD':[1, 2]}
categories_department = {
    'FOODS': {  
                1 : [ num for num in list(range(1, 220)) if num not in [7, 100, 165]],
                2: [ num for num in list(range(1, 400 )) if num not in [98]],
                3: [ num for num in list(range(1, 828)) if num not in [52, 699, 728, 740]]
            },

    'HOBBIES':{
                1 : [num for num in list(range(1, 425)) if num not in [59, 71, 96, 101, 182, 196, 222, 291]],
                2: list(range(1,150))
            },

    'HOUSEHOLD': {
                    1 : [num for num in list(range(1, 542)) if num not in [31, 41, 84, 111, 240, 273, 352, 391, 392]], 
                    2: [num for num in list(range(1, 517)) if num not in [181]]
                }
}