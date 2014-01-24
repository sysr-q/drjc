#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import random


class Stop(object):
	def __new__(cls, *args, **kwargs):
		if not hasattr(cls, "_stop_word"):
			cls._stop_word = super(Stop, cls).__new__(cls, *args, **kwargs)
		return cls._stop_word
	def __str__(self):
		return "<stop>"
	__repr__ = __str__


class Markov(object):
	def __init__(self, sources):
		self.sources = sources
		self.chain_length = 2
		self.max_words = 30
		self.length_cap = 200
		self.stop_word = Stop()
		self.markov = {}
		self.horse()

	def horse(self, sources=None, chain_length=None):
		if sources is None:
			sources = self.sources
		if chain_length is None:
			chain_length = self.chain_length
		for text in sources:
			self.markov_add(text, chain_length=chain_length)
	
	def markov_split(self, message, chain_length=None):
		if chain_length is None:
			chain_length = self.chain_length
		words = message.split()
		if len(words) < chain_length:
			return
		words.append(self.stop_word)
		for i in xrange(len(words) - chain_length):
			yield words[i:i+chain_length+1]
	
	def markov_add(self, message, chain_length=None):
		if chain_length is None:
			chain_length = self.chain_length
		for words in self.markov_split(message, chain_length=chain_length):
			key = tuple(words[:-1])
			self.markov.setdefault(key, [])
			self.markov[key].append(words[-1])
		return self.markov
	
	def markov_gen(self, max_words=None, length_cap=None, seed=None, chain_length=None):
		if max_words is None:
			max_words = self.max_words
		if length_cap is None:
			length_cap = self.length_cap
		if seed is None:
			seed = random.choice(self.sources)
		if chain_length is None:
			chain_length = self.chain_length
		key = seed.split()[:chain_length]
		gen_words = []
		for i in xrange(max_words - 1):
			gen_words.append(key[0])
			if len(" ".join(gen_words)) > length_cap:
				gen_words.pop(-1)
				break
			try:
				next_word = self.markov[tuple(key)]
			except KeyError:
				# RUN, GO, GET TO THE CHOPPA!
				break
			if not next_word:
				break
			next = random.choice(next_word)
			key = key[1:] + [next]
			if next is self.stop_word:
				gen_words.append(key[0])
				break
		message = " ".join(gen_words)
		return message.strip()
