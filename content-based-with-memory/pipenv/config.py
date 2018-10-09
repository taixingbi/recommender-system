'''
1. features saved in '/tmp'
2. features could be removed or added, not limited below
3. weight is range (0, 1), could be modified as you assume how important
'''
features=[# ('feature'          ,weight),  
            ('is_available'          ,1),
            ('is_rental'             ,1), 
            ('is_commercial'         ,1),
            ('rent'                  ,1),
            ('price'                 ,1),
            ('num_bedrooms'          ,1),
            ('area'                 ,.8),
            ('geo'                  ,.8),
            ('num_rooms'            ,.7),
            ('num_bathrooms'        ,.6),
            ('pets'                 ,.5),
            ('is_new_development'   ,.4),
            ('common_charges'       ,.3),
            ('is_furnished'         ,.3),
            ('headline'             ,.3),    
            ('financing_allowed'    ,.3)    
          ] 
