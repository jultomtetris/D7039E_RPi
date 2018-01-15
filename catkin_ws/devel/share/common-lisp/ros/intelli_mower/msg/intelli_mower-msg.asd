
(cl:in-package :asdf)

(defsystem "intelli_mower-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "MowerStats" :depends-on ("_package_MowerStats"))
    (:file "_package_MowerStats" :depends-on ("_package"))
  ))