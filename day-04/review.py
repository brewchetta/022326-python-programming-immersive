# Wednesday Review #

# Create a class `MovieReview` which has required attributes `movie_title:str`, `reviewer_name:str`, `score:int`, `date_reviewed:datetime.date`.
	# You may need to look up how to use `datetime.date` (hint: you'll need `from datetime import date`)

# Create a `__repr__`.

# Create an instance method `pretty_print()` which prints the review like so: `"<movie_title> review by <reviewer_name> on <date_reviewed>: <score> / 5 stars"`.
	# Example: `land_before_time.pretty_print()` >>> `"Land Before Time review by Fred Flintstone on 2014-4-12: 5/5 stars"`

# Create an instance method `increase_score()` which increases that movie's score by 1 but not above 5.

# Create an instance method `update_review()`. This accepts an argument of a `new_score` and optionally a `new_reviewer`. This updates the `score` and sets the `date_reviewed` to today.  If `new_reviewer` was passed this will also update the `reviewer_name` and if not it will retain the previous `reviewer_name`.
	# Example: `land_before_time.update_review(4)` # score changed to `4`, date becomes today, reviewer is still `"Fred Flinstone"`
	# Example: `land_before_time.update_review(5, "Littlefoot")` # score changed to `5`, date becomes today, reviewer becomes `"Littlefoot"`

# Create a class method `review_bomb()` which accepts a `movie_title` and `num_reviews`. This generates a review `num_reviews` times for the `movie_title` each with a `score` of 1, a `reviewer_name` of `Statler & Waldorf`, and a `date_reviewed` of today. Return all instances in a list.
	# Example: `MovieReview.review_bomb("Plan 9 From Outer Space", 10)` >>> creates 10 reviews for "Plan 9 From Outer Space"

# we are importing just `date` from the `datetime` module
from datetime import date

class MovieReview:
    
	def __init__(self, movie_title:str, reviewer_name:str="anonymous", score:int=0, date_reviewed:date=date.today()):
		self.movie_title = movie_title
		self.reviewer_name = reviewer_name
		self.score = min(score, 5)
		self.date_reviewed = date_reviewed

	def __repr__(self):
		return f"MovieReviewer(movie_title={self.movie_title}, reviewer_name={self.reviewer_name}, score={self.score}, date_reviewed={self.date_reviewed})"

	def pretty_print(self):
		return f"{self.movie_title} review by {self.reviewer_name} on {self.date_reviewed}: {self.score} / 5 stars"
	
	def increase_score(self):
		if self.score < 5:
			self.score += 1

	def update_review(self, new_score, new_reviewer=None):
		self.score = new_score
		self.date_reviewed = date.today()
		if new_reviewer: 
			self.reviewer_name = new_reviewer

	@classmethod
	def review_bomb(cls, movie_title:str, num_reviews:int):

		new_reviews_list = []

		for num in range(num_reviews):
			if num < 50:
				reviewer_name = "Chett"
			else:
				reviewer_name = "Sarah"

			# cls is a stand in for MovieReview
			new_review = cls(movie_title=movie_title, reviewer_name=reviewer_name, score=1, date_reviewed=date.today())
			
			new_reviews_list.append(new_review)

		return new_reviews_list


review_1 = MovieReview( movie_title="The Long Walk", reviewer_name="Bruce", score=20, date_reviewed=date.today() )

review_2 = MovieReview( movie_title="Sausage Party", reviewer_name="Steve", score=3, date_reviewed=date.today() )


# ADDITIONAL NOTES SECTION #

# default argument --> fallback if `name` isn't given
def whatever(name="anonymous"):
	pass

# type hints --> don't actually impact what can be taken in BUT they tell other devs what data type we're expecting
def something(name:str):
	# we can also enforce certain data types and raise errors if they're wrong
	if type(name) != str:
		raise TypeError("Name must be a string")