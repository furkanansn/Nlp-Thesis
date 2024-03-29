%%% FSA
initial(q0).
final(qn1).
final(qn2).
final(qn3).
final(qn4a).
final(qn4b).
final(qv1).
final(qv2).
final(qv3a).
final(qv3b).
final(qv3c).
final(qv3d).
final(qv4a).
final(qv4b).
final(qv5).

t(q0,noun,qn1).
t(qn1,plur,qn2).
t(qn1,poss,qn3).
t(qn1,loc,qn4a).
t(qn1,gen,qn4a).
t(qn1,acc,qn4b).
t(qn1,dat,qn4b).
t(qn1,abl,qn4b).
t(qn2,poss,qn3).
t(qn2,loc,qn4a).
t(qn2,gen,qn4a).
t(qn2,acc,qn4b).
t(qn2,dat,qn4b).
t(qn2,abl,qn4b).
t(qn3,loc,qn4a).
t(qn3,gen,qn4a).
t(qn3,acc,qn4b).
t(qn3,dat,qn4b).
t(qn4a,rel,qn1).

t(q0,verb,qv1).
t(qv1,neg,qv2).
t(qv1,t_def_past,qv3a).
t(qv1,t_indef_past,qv3b).
t(qv1,prog,qv3b).
t(qv1,aor,qv3b).
t(qv1,fut,qv3b).
t(qv1,nec,qv3b).
t(qv1,cond,qv3c).
t(qv1,opt,qv3d).
t(qv2,t_def_past,qv3a).
t(qv2,t_def_past,qv3b).
t(qv2,prog,qv3b).
t(qv2,aor,qv3b).
t(qv2,fut,qv3b).
t(qv2,nec,qv3b).
t(qv2,cond,qv3c).
t(qv2,opt,qv3d).
t(qv2,def_indic,qv5).
t(qv3a,def_indic,qv5).
t(qv3a,a_cond,qv4a).
t(qv3a,a_def_past,qv4a).
t(qv3b,indic,qv5).
t(qv3b,a_def_past,qv4a).
t(qv3b,a_cond,qv4a).
t(qv3b,a_indef_past,qv4b).
t(qv3c,a_def_past,qv4a).
t(qv3c,a_indef_past,qv4b).
t(qv3c,def_indic,qv5).
t(qv3d,a_def_past,qv4a).
t(qv3d,a_indef_past,qv4b).
t(qv3d,indic,qv5).
t(qv4a,def_indic,qv5).
t(qv4b,indic,qv5).

%%% Allamorphs
allomorph(git, verb).
allomorph(kalk, verb).
allomorph(bin, verb).
allomorph(geç, verb).
allomorph(dur, verb).

allomorph(ma,neg).
allomorph(me,neg).
allomorph(mı,neg).
allomorph(mi,neg).
allomorph(mu,neg).
allomorph(mü,neg).

allomorph(dı,t_def_past).
allomorph(di,t_def_past).
allomorph(tı,t_def_past).
allomorph(ti,t_def_past).
allomorph(du,t_def_past).
allomorph(dü,t_def_past).
allomorph(tu,t_def_past).
allomorph(tü,t_def_past).

allomorph(ün, ref).

allomorph(ma, neg).

allomorph(m,def_indic).
allomorph(n,def_indic).
allomorph(k,def_indic).
allomorph(nız,def_indic).
allomorph(niz,def_indic).
allomorph(nuz,def_indic).
allomorph(nüz,def_indic).
allomorph(ler,def_indic).
allomorph(lar,def_indic).

allomorph(mış,indef_past).
allomorph(miş,indef_past).
allomorph(muş,indef_past).
allomorph(müş,indef_past).

allomorph(ım,indic).
allomorph(im,indic).
allomorph(um,indic).
allomorph(üm,indic).
allomorph(sın,indic).
allomorph(sin,indic).
allomorph(sun,indic).
allomorph(sün,indic).
allomorph(ız,indic).
allomorph(iz,indic).
allomorph(uz,indic).
allomorph(üz,indic).
allomorph(sınız,indic).
allomorph(siniz,indic).
allomorph(sunuz,indic).
allomorph(sünüz,indic).
allomorph(ler,indic).
allomorph(lar,indic).

allomorph(mış,t_indef_past).
allomorph(miş,t_indef_past).
allomorph(muş,t_indef_past).
allomorph(müş,t_indef_past).

allomorph(ır,aor).
allomorph(ir,aor).
allomorph(ur,aor).
allomorph(ür,aor).
allomorph(ar,aor).
allomorph(er,aor).

allomorph(i,poss).
allomorph(ý,poss).
allomorph(u,poss).
allomorph(ü,poss).
allomorph(ým,poss).
allomorph(im,poss).
allomorph(um,poss).
allomorph(üm,poss).
allomorph(ýn,poss).
allomorph(in,poss).
allomorph(un,poss).
allomorph(ün,poss).
allomorph(ýmýz,poss).
allomorph(imiz,poss).
allomorph(umuz,poss).
allomorph(ümüz,poss).
allomorph(ýnýz,poss).
allomorph(iniz,poss).
allomorph(unuz,poss).
allomorph(ünüz,poss).
allomorph(larý,poss).
allomorph(leri,poss).
allomorph(si,poss).
allomorph(sý,poss).
allomorph(su,poss).
allomorph(sü,poss).
allomorph(m,poss).
allomorph(n,poss).
allomorph(mýz,poss).
allomorph(miz,poss).
allomorph(muz,poss).
allomorph(müz,poss).
allomorph(nýz,poss).
allomorph(niz,poss).
allomorph(nuz,poss).
allomorph(nüz,poss).

allomorph(i,acc).
allomorph(ý,acc).
allomorph(sý,acc).
allomorph(u,acc).
allomorph(ü,acc).

allomorph(den,abl).
allomorph(dan,abl).
allomorph(ten,abl).
allomorph(tan,abl).

allomorph(e,dat).
allomorph(ye,dat).
allomorph(a,dat).

allomorph(de,loc).
allomorph(da,loc).
allomorph(te,loc).
allomorph(ta,loc).

allomorph(in,gen).
allomorph(ýn,gen).
allomorph(un,gen).
allomorph(ün,gen).

allomorph(durak, noun).
allomorph(otobüs, noun).
allomorph(hat, noun).
allomorph(forum, noun).
allomorph(saat, noun).
allomorph(otogar, noun).
allomorph(süre, noun).
allomorph(fiyat, noun).
allomorph(hangi, noun).
allomorph(numara, noun).
allomorph(sefer, noun).
allomorph(kaçıncı, noun).
allomorph(öğrenci, noun).
allomorph(engelli, noun).

allomorph(ler, plur).
allomorph(lar, plur).

allomorph(meli,nec).
allomorph(malý,nec).

%% Inialize
analyze(String, AllomorphList):-
   initial(State),
   analyze(String, AllomorphList, State).

%% Finalize
analyze('', [], FinalState):-
   final(FinalState).

%% Recursive
analyze(String, [NormalizedPrefix|Rest_Allomorphs], CurrentState):-
   concat(Prefix, Suffix, String),
   check_softening(Prefix, NormalizedPrefix),
   allomorph(NormalizedPrefix, Morpheme),
   t(CurrentState, Morpheme, NextState),
   analyze(Suffix, Rest_Allomorphs, NextState).
   
   
check_softening(Prefix, NormalizedPrefix):-
   string_codes(Prefix, PrefixList),
   reverse(PrefixList, [PCode1|RestPCode]),
   char_code(PChar1, PCode1),
   (
      (
         ((PChar1 = ð); (PChar1 = g)),
         char_code(k, KCode),
         reverse(NormalizedPrefixList, [KCode|RestPCode]),
         string_codes(NormalizedPrefixStr, NormalizedPrefixList)

      );
      (
         (PChar1 = b),
         char_code(p, KCode),
         reverse(NormalizedPrefixList, [KCode|RestPCode]),
         string_codes(NormalizedPrefixStr, NormalizedPrefixList)

      );
      (
         (PChar1 = c),
         char_code(ç, KCode),
         reverse(NormalizedPrefixList, [KCode|RestPCode]),
         string_codes(NormalizedPrefixStr, NormalizedPrefixList)

      );
      (
         (PChar1 = d),
         char_code(t, KCode),
         reverse(NormalizedPrefixList, [KCode|RestPCode]),
         string_codes(NormalizedPrefixStr, NormalizedPrefixList)

      );
      (
         string_codes(NormalizedPrefixStr, PrefixList)
      )
   ),
   atom_string(NormalizedPrefix, NormalizedPrefixStr).
