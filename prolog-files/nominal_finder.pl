:- encoding(iso_latin_1).
:-include('D:/Thesis/prolog-files/morphophonologicalAnalyzer.pl').
:-include('D:/Thesis/prolog-files/tokenizer.pl').

generate_questions(List_of_Lists, Q_String):-
    generate_questions1(List_of_Lists, Q_List),
    lists_to_string(Q_List, Q_String).

generate_questions_units(String, List_of_Lists):-
    find_units(String, List_of_Lists).


lists_to_string([],'').
lists_to_string([List|Lists],String):-
    list_to_string(List,String1),
    lists_to_string(Lists, String2),
    concat(String1, ' ', String11),
    concat(String11,String2,String).
   
list_to_string([],'').
list_to_string([W|Ws],String):-
    list_to_string(Ws,String1),
    concat(W, ' ', W1),
    concat(W1, String1, String).

generate_questions1([List|Rest], [[Q]|Rest]):-
    reverse(List,[W|_]),
    analyze(W,L),
    reverse(L,[Last|_]),
    allomorph(Last,L1),
    
    (word(v1, [W]) -> find_Q1(L1, Q) ; find_Q(L1, Q) ).
   
% generate_questions1([List|Rest], [[Q|Ws]|Rest]):-
%     List = [A|Ws],
%     word(a, [A]),
%     Q = ka�.
%     
% generate_questions1([List|Rest], [[Q|Ws]|Rest]):-
%     List = [A|Ws],
%     word(a, [A]),
%     Q = hangi.
% 
generate_questions1([List|RestIN], [List|RestOUT]):-
    generate_questions1(RestIN, RestOUT).

find_Q(acc, neyi).
find_Q(acc, kimi).
find_Q(acc, hangisini).

find_Q(dat, neye).
find_Q(dat, nereye).

find_Q(noun, ne).
find_Q(noun, hangisi).

find_Q(tDefPast, 'ne yapt�').
find_Q(tProg, 'ne yap�yor').
find_Q(tFut, 'ne yapacak').

find_Q1(tAor, 'gidiyor mu'). % fiil al�n�p zaman ve soru ekleriyle birle�tirilecek
find_Q1(tAor, 'gider mi').

find_units(String,List_of_Lists):-
    tokenize(String, List_of_Words),
    find_units(List_of_Words,[],List_of_Lists).
find_units([],[],[]).
find_units([W|Ws],SubList,[List|List_of_Lists]):-
    (word(n, [W]); word(v, [W]); word(v1, [W])),
    append(SubList, [W], List),
    find_units(Ws,[],List_of_Lists).

find_units([W|Ws],SubList,List_of_Lists):-
    not(word(n, [W])), not(word(v, [W])), not(word(v1, [W])),
    append(SubList, [W], List),
    find_units(Ws,List,List_of_Lists).


word(n, [ne]).
word(n, [neye]).
word(n, [hangisi]).
word(n, [nereye]).
word(n, [ad�ye]).
word(n, [ad�den]).
word(a, [n_605]).
word(a, [numaral�]).
word(n, [otob�s]).
word(v1, [gitmektedir]).
word(n, [foruma]).
word(n, [otogara]).
word(a, [tren]).
word(n, [gar�na]).
word(n, [�ocuk]).
word(n, [k�pe�e]).
word(n, [k�pek]).
word(n, [kediyi]).
word(n, [kediye]).
word(n, [kedi]).
word(n, [kemik]).
word(a, [siyah]).
word(a, [beyaz]).
word(a, [b�y�k]).
word(a, [k���k]).
word(v, [havlad�]).
word(v, [havl�yor]).
word(v, [havlayacak]).
word(v1, [kovalad�]).
word(v, [koval�yor]).
word(v, [kovalayacak]).
word(v, [yedi]).
word(v, [verdi]).
word(v1, ['gider mi']).
word(v1, ['gidiyor mu']).

sinonim([ad�ye], [�niversiteye]).
sinonim([ad�ye], [ad�ye]).
sinonim([ad�ye], [kamp�se]).
sinonim([�niversiteye], [ad�ye]).
sinonim([foruma], [foruma]).
sinonim([foruma], ["forum-ayd�na"]).
sinonim([foruma], ["forum-avmye"]).
sinonim([otogara], [otogara]).



% ad�ye 605 numaral� otob�s gitmektedir