class Email:
	def __init__(self, to, sender, in_reply_to, references, subject, body, id, thread_id):
		self.to = to
		self.sender = sender
		self.in_reply_to = in_reply_to
		self.references = references
		self.subject = subject
		self.body = body
		self.id = id
		self.thread_id = thread_id
		
	def get_to(self):
		return self.to

	def get_sender(self):
		return self.sender

	def get_in_reply_to(self):
		return self.in_reply_to

	def get_references(self):
		return self.references

	def get_subject(self):
		return self.subject

	def get_body(self):
		return self.body

	def get_id(self):
		return self.id
	
	def get_thread_id(self):
		return self.thread_id

	def __str__(self):
 		return "to: " + self.to + " , " + "sender: " + self.sender + " , " + "in_reply_to: " + self.in_reply_to + " , " + "references: " + self.references + " , " + "subject: " + self.subject + " , " + "body: " + self.body + " , " + "id: " + self.id + " , " + "thread_id: " + self.thread_id
