#Dev Sprint 8#
##Intro to Rails##

#0. Install Rails if you haven't#

`gem install rails`

#1. Get to Know Rails#

Visit the [getting started tutorial](http://guides.rubyonrails.org/getting_started.html) at guides.rubyonrails.org. Give yourself a few hours to get through this; there is some Rails philosophy at the beginning and a lot of practice towards the end. This is going to be the foundation we build upon in week 9 when we create our own app from the ground up. Don't worry about a lot of the 'magic' you see; we will dig deeper when we do this next week. This is to get a taste of the way Rails is built, so that you will become familiar with the Rails vocabulary.

#2. Rails is not Ruby!#

Open the rails console (as described in #1 above). Try the following:
```
[[],nil,'',[nil]].each {|arg| puts "#{arg.blank?}"}
[[],nil,'',[nil]].each {|arg| puts "#{arg.present?}"}
[[],nil,'',[nil]].each {|arg| puts "#{arg.presence}"}
[1,'one',[1],['one'],nil].each {|arg| puts "#{arg.max}"}
[1,'one',[1],['one'],nil].each {|arg| puts "#{arg.try(:max)}"}
1.in?(1..3)
'alpha'.in?(['alpha','omega'])
Time.now
10.minutes.ago
Time.now - 10.hours
```

Many of these methods are very convenient...but do not actually exist in the ruby core. There's a whole article about it [here](http://guides.rubyonrails.org/active_support_core_extensions.html#extensions-to-date). 

Why point out that these methods are extensions of Ruby core? Well, many rails developers run into a problem when they start writing Ruby scripts and do not have access to the convenience methods in ActiveSupport. We'll do two (quick, promise!) exercises to illustrate this...

##Exercise 1: Triangles Redux##

Let's take the is_triangle? method from the dev-sprint7 repo and rewrite it using the rails convenience methods. Feel free to play around in console or check out the rails documentation of the [Array class](http://api.rubyonrails.org/classes/Array.html) for some inspiration.

##Exercise 2: Secret Messages##
###"htslwfyaqfyntsx ts ijhtinsl ymj xjhwjy rjxxflj!"###

The string above was encoded using ROT-5, an encryption method that rotates, or shifts, the letters by 5 in one direction or the other.

Write a class, called Crypto, with class methods, that can take a string and, given an integer 'n', provide the ROT-n version of that string. A basic start might be:
```
class Crypto
  # make all methods class methods, so we can call them
  # using Crypto.method(arguments)
  class << self
    # You will probably need to store some information about the alphabet in this class somehow...
    # maybe a hash?

    # You should be able to use the same method to encode and decode...keep in mind that
    # to decode a shift of 5 to the 'right', you will need to shift 5 to the 'left'
    def shift_message(message, shift_factor)
      #Your code here
    end
  end
end
```
Let me know how your coding adventure went by posting an encrypted line, along with the shift factor, at the end of your pull request for this sprint.

###Challenge###
Make it so your Crypto class doesn't barf when it runs into non-letters.
###Extra Challenge###
Make it so your Crypto class preserves capital and lowercase letters (this can be trivial depending on how you do the first Challenge...I recommend checking out Regexp...specifically, find out what `"A".match(/[A-Z]/)` does as opposed to `"a".match(/[a-z]/)`).

# Questions #
Remember if you have any questions, post them to [Piazza](https://piazza.com/class#spring2013/12).