tokenize(String,List):-
    remove_pre_blanks(String,String1),
    remove_post_blanks(String1,String2),
    tokenize1(String2,List).

tokenize1('',[]):- !.

tokenize1(String,[Word|Words]):-
    concat(Prefix,Suffix,String),
    (concat(Word,' ',Prefix);
    (Word = Prefix,Suffix == '')),!,
    tokenize1(Suffix,Words).

remove_32s([Code|Codes],[Code|Codes]):-
    not(Code == 32).
remove_32s([32|Rest],Codes):-
    remove_32s(Rest,Codes).
            
remove_special_characters(StringIN, StringOUT):-
    string_to_list(StringIN, ListIN),
    rm(ListIN, ListOUT),
    string_to_list(StringOUT, ListOUT).
    
rm([],[]).
rm([C|CsIN],[C|CsOUT]):-
    ((C >= 65, C =< 90); (C >= 97, C =< 122)),
    rm(CsIN, CsOUT).
    
rm([C|CsIN],CsOUT):-
    not((C >= 65, C =< 90); (C >= 97, C =< 122)),
    rm(CsIN, CsOUT).

remove_pre_blanks(StrIN,StrOUT):-
    string_to_list(StrIN,List1),
    remove_32s(List1,List2),
    string_to_list(StrOUT,List2).
    
remove_post_blanks(StrIN,StrOUT):-
    string_to_list(StrIN,List1),
    reverse(List1, RList1),
    remove_32s(RList1,RList2),
    reverse(RList2, List2),
    string_to_list(StrOUT,List2).