import sys
import re, os


class n:
    def __init__(self, v):
        self.v = v
        self.l = self.r = None

    def _nadd(self, v):

        if v > self.v:
            if self.r is None:
                self.r = n(v)
            else:
                self.r._nadd(v)
        elif v < self.v:
            if self.l is None:
                self.l = n(v)
            else:
                self.l._nadd(v)
        else:
            return

    def _inoprn(self):
        if self:
            _t = self
            if (_t.l):
                _t.l._inoprn()
            print _t.v
            if (_t.r):
                _t.r._inoprn()

    def _preprn(self):
        if self:
            _t = self
            print _t.v
            if (_t.l):
                _t.l._preprn()
            if (_t.r):
                _t.r._preprn()

    def _nrem(self, v):
        if self:
            if v < self.v:
                if self.l:
                    self.l = self.l._nrem(v)
                return self

            elif v > self.v:
                if self.r:
                    self.r = self.r._nrem(v)
                return self

            elif v == self.v:
                t = self
                if t.l is None and t.r is None:
                    t = None
                    return t
                elif t.l is None and t.r is not None:
                    t1 = t
                    t = t.r
                    t1 = None
                    return t


                elif t.r is None and t.l is not None:
                    t1 = t
                    t = t.l
                    t1 = None
                    return t
                else:
                    t1 = self._mval(t.r)
                    v1 = t1.v
                    t2 = self._nrem(v1)
                    t.v = v1

                    return t
            else:
                return self

    def _nrem2(self, t1):
        if t1:
            t1 = None
            return t1

    def _mval(self, t):
        if t:
            c = t
            while (c.l is not None):
                c = c.l
            return c
        else:
            return t

    def _height(self):
        lh = 0
        rh = 0
        if self is None:
            return 0
        else:
            if self.l:
                lh = self.l._height()
            if self.r:
                rh = self.r._height()

            if lh > rh :
                lh = lh+1
                return lh
            else:
                rh = rh+1
                return rh


class t:
    def __init__(self, h=None):
        self.h = h

    def _add(self, v):
        if self.h is None:
            self.h = n(v)
        else:
            t = self.h
            t._nadd(v)

    def _inop(self):
        if self.h is None:
            return
        else:
            pr = self.h
            pr._inoprn()

    def _prep(self):
        if self.h is None:
            return
        else:
            pr = self.h
            pr._preprn()

    def _rem(self, v):
        if self.h:
            t = self.h
            self.h = t._nrem(v)
            return self

    def _ht(self):
        if self.h:
            t = self.h
            return (t._height())

    def _bal(self):
        if self.h:
            t = self.h
            if t.l:
                ll =  (t.l._height())
            if t.r:
                rl = (t.r._height())
        return ll,rl


tr = t()

c = [10, 1, 5, 7, 40, 50, 2, 6 ,8 ,3, 7.25, 7.35, 5.5, 7.5]
for all in c:
    tr._add(all)

ht = tr._ht()
# check for balance
ll, rl = tr._bal()


if abs(ll-rl) > 1:
    print "tree unbalanced"
else:
    print "OK"