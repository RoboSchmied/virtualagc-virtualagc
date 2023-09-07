#!/usr/bin/env python3
'''
License:    The author, Ron Burkey, declares this program to be in the Public
            Domain, and may be used or modified in any way desired.
Filename:   SETTLIMI.py
Purpose:    This is part of the port of the original XPL source code for 
            HAL/S-FC into Python. 
Contact:    The Virtual AGC Project (www.ibiblio.org/apollo).
History:    2023-08-31 RSB  Ported from XPL
'''

from g import SDL_OPTION, SRN_PRESENT
from ERROR import ERROR
from HALINCL.CERRDECL import CLASS_B

'''
 /***************************************************************************/
 /* PROCEDURE NAME:  SET_T_LIMIT                                            */
 /* MEMBER NAME:     SETTLIMI                                               */
 /* FUNCTION RETURN TYPE:                                                   */
 /*          BIT(16)                                                        */
 /* INPUT PARAMETERS:                                                       */
 /*          LRECL             BIT(16)                                      */
 /* LOCAL DECLARATIONS:                                                     */
 /*          T_LIMIT           BIT(16)                                      */
 /* EXTERNAL VARIABLES REFERENCED:                                          */
 /*          SDL_OPTION                                                     */
 /*          CLASS_B                                                        */
 /*          SRN_PRESENT                                                    */
 /* EXTERNAL PROCEDURES CALLED:                                             */
 /*          ERROR                                                          */
 /* CALLED BY:                                                              */
 /*          INITIALIZATION                                                 */
 /***************************************************************************/
'''

def SET_T_LIMIT(LRECL):
    # Locals:
    T_LIMIT = 0
    
    if LRECL<0:
        ERROR(CLASS_B, 3);
    if SDL_OPTION:
        T_LIMIT=71;
    else:
        T_LIMIT=LRECL;
        if SRN_PRESENT:
            T_LIMIT=T_LIMIT-8;
    return T_LIMIT
